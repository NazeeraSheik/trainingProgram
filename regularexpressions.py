#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

#RegEx can be used to check if a string contains the specified search pattern.
import re 

txt="Hi i am Nazeera Sheik"
x=re.search("^Hi.*Sheik$",txt)
print(x)

#output
#<re.Match object; span=(0, 21), match='Hi i am Nazeera Sheik'>
#[Finished in 3.8s]

# []--->set of characters
# \-->special sequence
# .-->any character
# ^-->startswith
# $-->ends with
# *-->zero or more occurences
# +-->One or more occurrences
# ?-->Zero or one occurrences
# {}-->Exactly the specified number of occurrences
# |-->Either or
# ()-->Capture and group


paragraph='''If you are using Python on Windows for web development, 
we recommend a different set up for your development environment. 
Rather than installing directly on Windows, we recommend installing and using Python via the Windows Subsystem for Linux. 
For help, see: Get started using Python for web development on Windows. 
If you're interested in automating common tasks on your operating system,
see our guide: Get started using Python on Windows for scripting and automation. 
For some advanced scenarios (like needing to access/modify Python's installed files, make copies of binaries, or use Python DLLs directly), 
you may want to consider downloading a specific Python release directly from python.org or consider installing an alternative, such as Anaconda, Jython, PyPy, WinPython, IronPython, etc.
We only recommend this if you are a more advanced Python programmer with a specific reason for choosing an alternative implementation.'''

#using findall function
x = re.findall("Python", paragraph)
print(x)
# output
# ['Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python'] [Finished in 213ms]

x = re.findall("[a-zA-Z]", paragraph)
print(x)

# output
# ['I', 'f', 'y', 'o', 'u', 'a', 'r', 'e', 'u', 's', 'i', 'n', 'g', 'P', 'y', 't', 'h', 'o', 'n', 'o', 'n', 'W', 'i', 'n', 'd', 'o', 'w', 's', 'f', 'o', 'r', 'w', 'e', 'b', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'm', 'e', 'n', 't', 'w', 'e', 'r', 'e', 'c', 'o', 'm', 'm', 'e', 'n', 'd', 'a', 'd', 'i', 'f', 'f', 'e', 'r', 'e', 'n', 't', 's', 'e', 't', 'u', 'p', 'f', 'o', 'r', 'y', 'o', 'u', 'r', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'm', 'e', 'n', 't', 'e', 'n', 'v', 'i', 'r', 'o', 'n', 'm', 'e', 'n', 't', 'R', 'a', 't', 'h', 'e', 'r', 't', 'h', 'a', 'n', 'i', 'n', 's', 't', 'a', 'l', 'l', 'i', 'n', 'g', 'd', 'i', 'r', 'e', 'c', 't', 'l', 'y', 'o', 'n', 'W', 'i', 'n', 'd', 'o', 'w', 's', 'w', 'e', 'r', 'e', 'c', 'o', 'm', 'm', 'e', 'n', 'd', 'i', 'n', 's', 't', 'a', 'l', 'l', 'i', 'n', 'g', 'a', 'n', 'd', 'u', 's', 'i', 'n', 'g', 'P', 'y', 't', 'h', 'o', 'n', 'v', 'i', 'a', 't', 'h', 'e', 'W', 'i', 'n', 'd', 'o', 'w', 's', 'S', 'u', 'b', 's', 'y', 's', 't', 'e', 'm', 'f', 'o', 'r', 'L', 'i', 'n', 'u', 'x', 'F', 'o', 'r', 'h', 'e', 'l', 'p', 's', 'e', 'e', 'G', 'e', 't', 's', 't', 'a', 'r', 't', 'e', 'd', 'u', 's', 'i', 'n', 'g', 'P', 'y', 't', 'h', 'o', 'n', 'f', 'o', 'r', 'w', 'e', 'b', 'd', 'e', 'v', 'e', 'l', 'o', 'p', 'm', 'e', 'n', 't', 'o', 'n', 'W', 'i', 'n', 'd', 'o', 'w', 's', 'I', 'f', 'y', 'o', 'u', 'r', 'e', 'i', 'n', 't', 'e', 'r', 'e', 's', 't', 'e', 'd', 'i', 'n', 'a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'n', 'g', 'c', 'o', 'm', 'm', 'o', 'n', 't', 'a', 's', 'k', 's', 'o', 'n', 'y', 'o', 'u', 'r', 'o', 'p', 'e', 'r', 'a', 't', 'i', 'n', 'g', 's', 'y', 's', 't', 'e', 'm', 's', 'e', 'e', 'o', 'u', 'r', 'g', 'u', 'i', 'd', 'e', 'G', 'e', 't', 's', 't', 'a', 'r', 't', 'e', 'd', 'u', 's', 'i', 'n', 'g', 'P', 'y', 't', 'h', 'o', 'n', 'o', 'n', 'W', 'i', 'n', 'd', 'o', 'w', 's', 'f', 'o', 'r', 's', 'c', 'r', 'i', 'p', 't', 'i', 'n', 'g', 'a', 'n', 'd', 'a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'o', 'n', 'F', 'o', 'r', 's', 'o', 'm', 'e', 'a', 'd', 'v', 'a', 'n', 'c', 'e', 'd', 's', 'c', 'e', 'n', 'a', 'r', 'i', 'o', 's', 'l', 'i', 'k', 'e', 'n', 'e', 'e', 'd', 'i', 'n', 'g', 't', 'o', 'a', 'c', 'c', 'e', 's', 's', 'm', 'o', 'd', 'i', 'f', 'y', 'P', 'y', 't', 'h', 'o', 'n', 's', 'i', 'n', 's', 't', 'a', 'l', 'l', 'e', 'd', 'f', 'i', 'l', 'e', 's', 'm', 'a', 'k', 'e', 'c', 'o', 'p', 'i', 'e', 's', 'o', 'f', 'b', 'i', 'n', 'a', 'r', 'i', 'e', 's', 'o', 'r', 'u', 's', 'e', 'P', 'y', 't', 'h', 'o', 'n', 'D', 'L', 'L', 's', 'd', 'i', 'r', 'e', 'c', 't', 'l', 'y', 'y', 'o', 'u', 'm', 'a', 'y', 'w', 'a', 'n', 't', 't', 'o', 'c', 'o', 'n', 's', 'i', 'd', 'e', 'r', 'd', 'o', 'w', 'n', 'l', 'o', 'a', 'd', 'i', 'n', 'g', 'a', 's', 'p', 'e', 'c', 'i', 'f', 'i', 'c', 'P', 'y', 't', 'h', 'o', 'n', 'r', 'e', 'l', 'e', 'a', 's', 'e', 'd', 'i', 'r', 'e', 'c', 't', 'l', 'y', 'f', 'r', 'o', 'm', 'p', 'y', 't', 'h', 'o', 'n', 'o', 'r', 'g', 'o', 'r', 'c', 'o', 'n', 's', 'i', 'd', 'e', 'r', 'i', 'n', 's', 't', 'a', 'l', 'l', 'i', 'n', 'g', 'a', 'n', 'a', 'l', 't', 'e', 'r', 'n', 'a', 't', 'i', 'v', 'e', 's', 'u', 'c', 'h', 'a', 's', 'A', 'n', 'a', 'c', 'o', 'n', 'd', 'a', 'J', 'y', 't', 'h', 'o', 'n', 'P', 'y', 'P', 'y', 'W', 'i', 'n', 'P', 'y', 't', 'h', 'o', 'n', 'I', 'r', 'o', 'n', 'P', 'y', 't', 'h', 'o', 'n', 'e', 't', 'c', 'W', 'e', 'o', 'n', 'l', 'y', 'r', 'e', 'c', 'o', 'm', 'm', 'e', 'n', 'd', 't', 'h', 'i', 's', 'i', 'f', 'y', 'o', 'u', 'a', 'r', 'e', 'a', 'm', 'o', 'r', 'e', 'a', 'd', 'v', 'a', 'n', 'c', 'e', 'd', 'P', 'y', 't', 'h', 'o', 'n', 'p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r', 'w', 'i', 't', 'h', 'a', 's', 'p', 'e', 'c', 'i', 'f', 'i', 'c', 'r', 'e', 'a', 's', 'o', 'n', 'f', 'o', 'r', 'c', 'h', 'o', 'o', 's', 'i', 'n', 'g', 'a', 'n', 'a', 'l', 't', 'e', 'r', 'n', 'a', 't', 'i', 'v', 'e', 'i', 'm', 'p', 'l', 'e', 'm', 'e', 'n', 't', 'a', 't', 'i', 'o', 'n']
# [Finished in 221ms]


x = re.search("\s", paragraph)
print(x.start())

#output
# 2 [Finished in 235ms]


x = re.split("\s",paragraph)
print(x)

#output
# ['If', 'you', 'are', 'using', 'Python', 'on', 'Windows', 'for', 'web', 'development,', '', 'we', 'recommend', 'a', 'different', 'set', 'up', 'for', 'your', 'development', 'environment.', '', 'Rather', 'than', 'installing', 'directly', 'on', 'Windows,', 'we', 'recommend', 'installing', 'and', 'using', 'Python', 'via', 'the', 'Windows', 'Subsystem', 'for', 'Linux.', '', 'For', 'help,', 'see:', 'Get', 'started', 'using', 'Python', 'for', 'web', 'development', 'on', 'Windows.', '', 'If', "you're", 'interested', 'in', 'automating', 'common', 'tasks', 'on', 'your', 'operating', 'system,', 'see', 'our', 'guide:', 'Get', 'started', 'using', 'Python', 'on', 'Windows', 'for', 'scripting', 'and', 'automation.', '', 'For', 'some', 'advanced', 'scenarios', '(like', 'needing', 'to', 'access/modify', "Python's", 'installed', 'files,', 'make', 'copies', 'of', 'binaries,', 'or', 'use', 'Python', 'DLLs', 'directly),', '', 'you', 'may', 'want', 'to', 'consider', 'downloading', 'a', 'specific', 'Python', 'release', 'directly', 'from', 'python.org', 'or', 'consider', 'installing', 'an', 'alternative,', 'such', 'as', 'Anaconda,', 'Jython,', 'PyPy,', 'WinPython,', 'IronPython,', 'etc.', 'We', 'only', 'recommend', 'this', 'if', 'you', 'are', 'a', 'more', 'advanced', 'Python', 'programmer', 'with', 'a', 'specific', 'reason', 'for', 'choosing', 'an', 'alternative', 'implementation.']
# [Finished in 185ms]