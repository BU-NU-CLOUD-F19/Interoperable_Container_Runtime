Source Projects:
https://github.com/kubernetes/frakti - base  
https://github.com/hyperhq/runv - used to run hypervisors  
https://github.com/hyperhq/hyperd - API wrapper for runV  
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/node/runtime-client-server.md - proposed implementation of the runtime interface; currently reviewing docs and testing acutal implementation against this  
https://kubernetes.github.io/frakti/deploy.html - Deployment Instructions  
https://github.com/kubernetes/frakti/blob/master/docs/e2e-tests.md - End-to-End test instructions  
https://kubernetes.io/blog/2016/05/hypernetes-security-and-multi-tenancy-in-kubernetes/ - Hypernetes blog post  

Installation requires hyperd, docker, CNI, and kublet to also be installed on all notes  

Need to find - directory structure, esp. where rootfs and config.json are stored, as well as images, runtime states of running containers/pods  

