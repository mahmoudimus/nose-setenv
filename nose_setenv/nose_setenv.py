from __future__ import unicode_literals

import ast
import os

import nose
from nose.plugins import Plugin


class SetEnvironmentVariables(Plugin):
    """
    This plugin is used to set environment variables to seamlessly integrate
    in the nosetests architecture.

    """

    # required attributes by nose
    enabled = True
    name = 'env-setter'

    def options(self, parser, env):
        super(SetEnvironmentVariables, self).options(parser, env=env)
        parser.add_option(
            '--set-env-variables',
            dest='set_env_variables',
            default=None,
            help='The environment variables to set/override',
        )

    def configure(self, options, conf):
        super(SetEnvironmentVariables, self).configure(options, conf)

        if not options.set_env_variables:
            return

        env_variables_to_override = ast.literal_eval(options.set_env_variables)
        for env_key, env_val in env_variables_to_override.iteritems():
            os.environ[env_key] = env_val


if __name__ == '__main__':
    nose.main(addplugins=[SetEnvironmentVariables()])
