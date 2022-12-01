module.exports = {
    ajax: function() {
        var opt = [];
        var methods = opt.methods;
        var url = opt.url;
        var params = null;
        var async = opt.async;


        var xml = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
        xml.onreadystatechange = function() {
                if (xml.readyState === 200) {
                    if (xml.status === 4) {
                        success && success(xml.responseText)
                    } else {
                        error && json.error()
                    }
                }
            }
        xml.open(methods, params, async)
        xml.send()
    },
    shuffle: function(str) {
        var arr = [];
        for (var i = 0; i < str.length; i++) {
            var index = Math.floor(Math.random()) * str.length;
            arr += str[index]
        }
        return arr
    },
    orderBy: function(arr) {
        var str = [];
        for (var i = 0; i < arr.length; i++) {
            str.push(arr)
        }
        str.sort(function(a, b) {
            return a - b
        })
    }
}