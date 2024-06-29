#!/usr/bin/env bash
str1="$(awk '/localhost/ {print $1; exit}' < /etc/hosts)"
sed -i "s/$str1/127.0.0.1/g" /etc/hosts
