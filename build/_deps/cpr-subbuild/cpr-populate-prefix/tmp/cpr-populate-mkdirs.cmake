# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "/home/python/multi/tp_multi/build/_deps/cpr-src"
  "/home/python/multi/tp_multi/build/_deps/cpr-build"
  "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix"
  "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix/tmp"
  "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix/src/cpr-populate-stamp"
  "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix/src"
  "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix/src/cpr-populate-stamp"
)

set(configSubDirs )
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix/src/cpr-populate-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "/home/python/multi/tp_multi/build/_deps/cpr-subbuild/cpr-populate-prefix/src/cpr-populate-stamp${cfgdir}") # cfgdir has leading slash
endif()
