#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: Creates or updates a text file on a managed host.

options:
    path:
        description: Absolute or relative path to the target file.
        required: true
        type: path
    content:
        description:
            - Text to write into the target file.
        required: true
        type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
# extends_documentation_fragment:
#     - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Create a text file
  my_own_module:
    path: /tmp/example.txt
    content: Hello, Netology!
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
path:
    description: Path of the created or updated file.
    type: str
    returned: always
changed:
    description: Whether the file content was changed.
    type: bool
    returned: always
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='path', required=True),
        content=dict(type='str', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    # result = dict(
    #     changed=False,
    #     original_message='',
    #     message=''
    # )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    path = module.params['path']
    content = module.params['content']

    # # if the user is working with this module in only check mode we do not
    # # want to make any changes to the environment, just return the current
    # # state with no modifications
    # if module.check_mode:
    #     module.exit_json(**result)

    # # manipulate or modify the state as needed (this is going to be the
    # # part where your module will do what it needs to do)
    # result['original_message'] = module.params['name']
    # result['message'] = 'goodbye'

    # # use whatever logic you need to determine whether or not this module
    # # made any modifications to your target
    # if module.params['new']:
    #     result['changed'] = True

    # # during the execution of the module, if there is an exception or a
    # # conditional state that effectively causes a failure, run
    # # AnsibleModule.fail_json() to pass in the message and the result
    # if module.params['name'] == 'fail me':
    #     module.fail_json(msg='You requested this to fail', **result)

    # # in the event of a successful module execution, you will want to
    # # simple AnsibleModule.exit_json(), passing the key/value results
    # module.exit_json(**result)

    try:
        with open(path, 'r') as file_obj:
            old_content = file_obj.read()
    except FileNotFoundError:
        old_content = None
    except OSError as exc:
        module.fail_json(msg='Unable to read {0}: {1}'.format(path, exc))

    changed = old_content != content
    result = dict(changed=changed, path=path)

    if module.check_mode or not changed:
        module.exit_json(**result)

    try:
        with open(path, 'w') as file_obj:
            file_obj.write(content)
    except OSError as exc:
        module.fail_json(msg='Unable to write {0}: {1}'.format(path, exc), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
