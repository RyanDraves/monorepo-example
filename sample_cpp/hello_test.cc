#include <gtest/gtest.h>

#include "hello.h"

TEST(HelloTest, BasicAssertions) {
  EXPECT_STREQ(hello(1).c_str(), "hello");
  EXPECT_STREQ(hello(2).c_str(), "hellohello");
}
