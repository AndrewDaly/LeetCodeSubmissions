import subprocess

status_command = subprocess.check_output(["git", "status"])
print("status_command line:" + str(status_command))

add_command = subprocess.check_output(["git", "add", "."])
print("add_command line:" + str(add_command))

commit_command = subprocess.check_output(["git", "commit", '-m "this is a python git command"'])
print(commit_command)

push_command = subprocess.check_output(["git", "push"])
print(push_command)


# process = subprocess.Popen(["git", "status"], stdout=subprocess.PIPE)
# print("second print line: " + str(process))
# output = process.communicate()[0]
# print("third print line: " + str(output))


