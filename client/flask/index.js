let {PythonShell} = require('python-shell')

PythonShell.run("app_testing.py",null,function(err,results){
    console.log(results)
    console.log("Python script finished")
})