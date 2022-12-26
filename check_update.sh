#!/bin/sh
# Make sure we don't pick up 0.3.95 (which is 3 years older than 0.3.3)
git ls-remote --tags https://github.com/lensfun/lensfun |grep 'refs/tags/v' |grep -v 0.3.95 |grep -v '\^{}' |grep -viE '(alpha|beta|RC)' |sed -e 's,.*refs/tags/v,,' |sort -V |tail -n1

