#include <iostream>
#include <string>

#include "hello.h"

std::string hello(int x) {
  static const std::string msg = "hello";
  std::string result;
  for (int i = 0; i < x; ++i) {
      result += msg;
  }
  return result;
}
