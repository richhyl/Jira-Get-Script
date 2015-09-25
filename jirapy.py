import sys, jira

try:
   authed_jira = jira.JIRA('https://jira.atlassian.com/') # , basic_auth=('richard.hylands', 'c0ntract7ester')
except jira.utils.JIRAError as e:
   print e.text
   sys.exit()

issues = authed_jira.search_issues('')

with open("data.csv", "w") as f:
  for issue in issues:
    columns = [issue.fields.project.key, issue.fields.issuetype.name, issue.fields.reporter.displayName]
    f.write(",".join(columns))
    f.write("\n")

import json
all_issues = []
for issue in issues:
  issue_data = {"key": issue.fields.project.key, "name": issue.fields.issuetype.name, "displayName": issue.fields.reporter.displayName}
  all_issues.append(issue_data)

print json.dumps(all_issues)