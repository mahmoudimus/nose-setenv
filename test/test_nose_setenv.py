import optparse
import os
import unittest

from nose.config import Config

from nose_setenv import SetEnvironmentVariables


class TestNoseSetEnv(unittest.TestCase):
    def test_configure_it_should_set_configured(self):
        set_environment_variables = SetEnvironmentVariables()
        parser = optparse.OptionParser()
        env = os.environ
        set_environment_variables.options(parser, env)
        options, _ = parser.parse_args(["--set-env-variables={'blah': 'foo'}"])
        config = Config()

        set_environment_variables.configure(options, config)

        self.assertEquals(os.environ.get('blah'), 'foo')
