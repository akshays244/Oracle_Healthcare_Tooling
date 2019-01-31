def execute_command(command):
    print("command %s execution started" %command)
    try:
        ret = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except Exception as e:
        print("Failed to execute script error_msg: %s"%(e))
    out, err = ret.communicate()
    returncode = ret.wait()
    if returncode != 0:
        print("Failed to excuete command %s output: %s" %(command, out))
        sys.exit(1)
    print("command %s excueted successfully" %(command))
    return (out, err, returncode)
