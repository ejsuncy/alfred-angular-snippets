#!/usr/bin/python
# encoding: utf-8

import sys
import re
from workflow import Workflow3
import json

__version__ = '0.1'
__github_slug__ = 'ejsuncy/alfred-angular-snippets.git'

log = None

var_regex = re.compile("\${(.*?):(.*?)}")
cursor_regex = re.compile("\$0")

def main(wf):
    query = sys.argv[1].split()
    keyword = query[0]

    if (keyword):

        results = wf.filter(keyword, snippets.keys())

        for result in results:
            snippet_name = result
            snippet_description = snippets[result]['description']
            snippet_body = "\n".join(snippets[result]['body'])

            subtitle = snippet_description
            valid = True
            autocomplete = result

            # if len(query) > 1:
            #     subtitle += ": add %s" % snippet_name
            #     valid = True
            #     autocomplete = None

            item = wf.add_item(title=snippet_name,
                    subtitle=subtitle,
                    valid=valid,
                    arg="potato",
                    autocomplete=autocomplete)

            # var_names = []

            # name = query[1] # after snippet keyword, the next arg is always the name
            # Name = [name[0].upper() if len(name) == 1 else name[0].upper() + name[1:]][0]

            match_iter = var_regex.finditer(snippet_body) # finds all the variables of pattern ${1:varname}

            # if len(query) > 1:
            for match in match_iter:
                var_index_str, var_name = match.group(1,2)
                var_index = int(var_index_str)
                var_string = re.escape(match.group(0))
                snippet_body = re.sub(var_string, "%s" % var_name, snippet_body) # replace ${1:varname} with varname (VS Code -> alfred)

                # if "name" == var_string:
                #     var_name_value = name
                # elif "Name" == var_string:
                #     var_name_value = Name
                # elif "ServiceName" == var_string:
                #     var_name_value = Name
                # elif "eventName" == var_string:
                #     var_name_value = name

                # if var_name == "selector-name":
                #     var_name = "selectorName"
                #     item.setvar(var_name, 'selector-' + str(query[var_index]).lower())
                # elif var_name == "Name":
                #     uppercased = query[var_index][0].upper()

                #     if len(query[var_index]) > 1:
                #         uppercased += query[var_index][1:]

                #     item.setvar(var_name, uppercased)
                # else:
                #     var_name = var_name.replace("-", "")
                #     item.setvar(var_name, query[var_index])

                # var_names.append(var_name)

            snippet_body = re.sub(cursor_regex, "{cursor}", snippet_body)
            item.setvar('snippetBody', snippet_body)
            # item.setvar('varNames', " ".join(var_names))

    wf.send_feedback()

def get_snippets():
    snippets = {}

    with open("snippets/typescript.json") as f:
        json_str = f.read()
        snippets.update(json.loads(json_str))

    with open("snippets/html.json") as f:
        json_str = f.read()
        snippets.update(json.loads(json_str))

    return snippets

if __name__ == '__main__':
    update_settings = {
        'github_slug':  __github_slug__,
        'version':      __version__
    }

    wf = Workflow3(libraries=['./lib'], update_settings = update_settings)

    if wf.update_available:
        wf.start_update()
        wf.clear_cache()

    global snippets
    snippets = wf.cached_data('snippets', get_snippets, max_age=0)


    # Assign Workflow logger to a global variable for convenience
    log = wf.logger
    sys.exit(wf.run(main))

