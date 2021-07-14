import subprocess as sb
x = sb.getoutput(kubectl get pods)
print(x)
