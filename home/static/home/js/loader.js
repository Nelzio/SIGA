const sleep = time => new Promise(resolve => {
            setTimeout(resolve, time)
        });

        const louderAction = async() => {
            //document.getElementById("loaderPageStart").style.minHeight = '10000000'

            await sleep(500)
        }
        louderAction().then(() => document.getElementById("loaderPageStart").innerHTML = "<div class=''></div>");