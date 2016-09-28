#!/bin/bash
mkdir -p spack && cd spack && curl -L https://github.com/LLNL/spack/tarball/develop | tar -x -z -v --strip-components 1 -f  - && cd -
. spack/share/spack/setup-env.sh
spack compiler rm gcc@4.9.3
mkdir -p hep-spack && cd hep-spack && curl -L https://github.com/gartung/hep-spack/tarball/master | tar -x -z -v --strip-components 1 -f  - && cd -
spack repo rm hsf
spack repo add $PWD/hep-spack
mkdir -p artstack-spack && cd artstack-spack && curl -L https://github.com/gartung/artstack-spack/tarball/master | tar -x -z -v --strip-components 1 -f  - && cd -
spack repo rm artstack
spack repo add $PWD/artstack-spack
if [[ $OSTYPE != linux-gnu ]]; then
   SYSCOMP=`clang -v 2>&1 | grep clang | awk '{print "clang@"$4"-apple"}'`
else
   spack compiler add /usr/bin
   sed -i.bak -e 's!/lib64/ccache!/bin!g' ~/.spack/compilers.yaml
   sed -i.bak -e 's!/lib64/ccache!/bin!g' spack/etc/spack/compilers.yaml
   SYSCOMP=`gcc -v 2>&1 | grep "(GCC)" | awk '{print $1"@"$3}'`
fi
spack mirror rm home
spack mirror add home http://home.fnal.gov/~gartung/spack_mirror
if [[ $OSTYPE == linux-gnu ]]; then
spack install "gcc@4.9.3+binutils+gold%"$SYSCOMP
here=`spack location -i gcc@4.9.3%$SYSCOMP`
spack compiler add $here
else
spack install "gcc@4.9.3~binutils~gold%"$SYSCOMP
here=`spack location -i gcc@4.9.3%$SYSCOMP`
spack compiler add $here
fi
spack install canvas@gcc@4.9.3
