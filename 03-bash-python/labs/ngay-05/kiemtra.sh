#!/bin/bash
if [ -f "$1" ]; then
  echo "File '$1' tồn tại."
else
  echo "Không tìm thấy '$1'."
fi
