"use strict";
function _typeof(obj) {
    return (_typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function(obj) {
        return typeof obj
    }
    : function(obj) {
        return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj
    }
    )(obj)
}
var customReport;
function randomString(len) {
    len = len || 10;
    for (var $chars = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz123456789", maxPos = $chars.length, pwd = "", i = 0; i < len; i++)
        pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
    return pwd + (new Date).getTime()
}
function performanceReport(option, fn) {
    try {
        var reportData = function(argument_0, argument_1, argument_2) {
            var type = 0 < arguments.length && void 0 !== argument_0 ? argument_0 : 1
              , actionName = 1 < arguments.length ? argument_1 : void 0
              , subType = 2 < arguments.length ? argument_2 : void 0;
            opt.isPerformance && perforPage(),
            (opt.isResource || opt.isAjax) && perforResource(),
            ERRORLIST && ERRORLIST.length && (conf.errorList = conf.errorList.concat(ERRORLIST));
            var w = window.screen.width
              , h = window.screen.height
              , markuser = function() {
                var markUser = sessionStorage.getItem("bs_markUser") || ""
                  , result = {
                    markUser: markUser,
                    isFristIn: !1
                };
                return markUser || (markUser = randomString(),
                sessionStorage.setItem("bs_markUser", markUser),
                result.markUser = markUser,
                result.isFristIn = !0),
                result
            }()
              , result = {
                time: (new Date).getTime(),
                addData: ADDDATA,
                markUser: markuser.markUser,
                type: type,
                url: location.href,
                pv: function(url) {
                    if ("/" == url)
                        return "/";
                    var ps = url.indexOf("undefined") || -1;
                    return (url = 0 < ps ? url.substring(0, ps + 9) : url).match(/(\/)?([a-zA-Z-_0-9~])+(\/)?/g).map(function(item) {
                        return item = 18 <= item.length && /\d{6,}([A-Z]+)?[a-z]+/.test(item.split("/")[0].split("").filter(function(item) {
                            return /\d|[A-Z]|[a-z]/.test(item)
                        }).sort().join("")) ? "encryptedString/" : item
                    }).join("")
                }(function(href) {
                    var originLen = location.origin.length;
                    return href.includes("?") ? href.substring(originLen).split("?")[0] : href.includes("&") ? href.substring(originLen).split("&")[0] : href.substring(originLen)
                }(location.href)),
                markUv: function() {
                    var date = new Date
                      , markUv = localStorage.getItem("bs_markUv") || ""
                      , datatime = localStorage.getItem("bs_markUvTime") || ""
                      , today = date.getFullYear() + "/" + (date.getMonth() + 1) + "/" + date.getDate() + " 23:59:59";
                    return (!markUv && !datatime || date.getTime() > 1 * datatime) && (markUv = randomString(),
                    localStorage.setItem("bs_markUv", markUv),
                    localStorage.setItem("bs_markUvTime", new Date(today).getTime())),
                    markUv
                }()
            };
            !function() {
                var reslist = conf.resourceList
                  , filterUrl = opt.filterUrl
                  , newlist = [];
                if (reslist && reslist.length && filterUrl && filterUrl.length)
                    for (var i = 0; i < reslist.length; i++) {
                        for (var begin = !1, j = 0; j < filterUrl.length; j++)
                            if (-1 < reslist[i].name.indexOf(filterUrl[j])) {
                                begin = !0;
                                break
                            }
                        begin || newlist.push(reslist[i])
                    }
                conf.resourceList = newlist
            }(),
            1 === type ? result = Object.assign(result, {
                preUrl: conf.preUrl,
                performance: conf.performance,
                resourceList: conf.resourceList,
                isFristIn: markuser.isFristIn,
                screenwidth: w,
                screenheight: h
            }) : 2 === type ? result = Object.assign(result, {
                resourceList: conf.resourceList,
                errorList: conf.errorList
            }) : 3 === type ? result = Object.assign(result, {
                errorList: conf.errorList,
                resourceList: conf.resourceList
            }) : 4 === type && (actionName && (opt.action = actionName + ""),
            result = Object.assign(result, {
                resourceList: conf.resourceList
            })),
            result = Object.assign(result, opt.add),
            fn && fn(result);
            var reportedData = {
                identity: 1,
                clientInfo: {
                    model: navigator.userAgent,
                    screen: JSON.stringify({
                        width: w,
                        height: h
                    })
                },
                items: [{
                    action: 1 === type ? "action_js_performance" : opt.action || "action_js_monitor",
                    p: JSON.stringify({
                        appKey: opt.appKey,
                        time: result.time,
                        type: function(type, result, subType) {
                            var errorSubtype = "";
                            if (2 < type) {
                                errorSubtype = result.errorList && 0 < result.errorList.length ? result.errorList[0].data.status : "otherError";
                                for (var httpResponseCode = [500, 400, 300, 200, 100], errorType = ["50X", "40X", "30X", "20X", "10x"], i = 0; i < httpResponseCode.length; i++)
                                    httpResponseCode[i] <= errorSubtype && (errorSubtype = errorType[i]);
                                errorSubtype = subType && "" != subType ? subType : errorSubtype
                            }
                            return errorSubtype
                        }(type, result, subType),
                        pv: result.pv,
                        uv: result.markUv,
                        from: "apmsdk"
                    }),
                    p2: JSON.stringify({
                        url: result.url
                    }),
                    p3: result.errorList ? JSON.stringify(result.errorList) : "",
                    p4: result.performance ? JSON.stringify(result.performance) : "",
                    p5: result.resourceList ? JSON.stringify(result.resourceList) : "",
                    p6: JSON.stringify({
                        os: function() {
                            var OS = ""
                              , OSArray = {}
                              , UserAgent = navigator.userAgent.toLowerCase();
                            for (var i in OSArray.Windows = "Win32" == navigator.platform || "Windows" == navigator.platform,
                            OSArray.Mac = "Mac68K" == navigator.platform || "MacPPC" == navigator.platform || "Macintosh" == navigator.platform || "MacIntel" == navigator.platform,
                            OSArray.iOS = -1 < UserAgent.indexOf("iphone") || -1 < UserAgent.indexOf("ipad"),
                            OSArray.android = -1 < UserAgent.indexOf("android"),
                            OSArray.harmony = -1 < UserAgent.indexOf("harmony"),
                            OSArray)
                                OSArray[i] && (OS = i);
                            return OS
                        }(),
                        browser: function() {
                            var UserAgent = navigator.userAgent.toLowerCase()
                              , browser = null
                              , browserArray = {
                                IE: window.ActiveXObject || "ActiveXObject"in window,
                                Chrome: -1 < UserAgent.indexOf("chrome") && -1 < UserAgent.indexOf("safari"),
                                Firefox: -1 < UserAgent.indexOf("firefox"),
                                Opera: -1 < UserAgent.indexOf("opera"),
                                Safari: -1 < UserAgent.indexOf("safari") && -1 == UserAgent.indexOf("chrome"),
                                Edge: -1 < UserAgent.indexOf("edge"),
                                QQBrowser: /qqbrowser/.test(UserAgent),
                                WeixinBrowser: /MicroMessenger/i.test(UserAgent)
                            };
                            for (var i in browserArray)
                                browserArray[i] && (browser = i);
                            return browser
                        }(),
                        ua: navigator.userAgent
                    }),
                    p7: ADDDATA ? JSON.stringify(result.addData) : ""
                }]
            };
            !fn && window.fetch ? fetch(opt.domain, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json;charset=UTF-8",
                    "report-source": "apmsdk-fetch-v" + window.APMSDKVERSION
                },
                type: "report-data",
                body: JSON.stringify(reportedData)
            }) : ajax({
                url: opt.domain,
                type: "POST",
                async: !0,
                data: JSON.stringify(reportedData),
                dataType: "json",
                success: function(data) {}
            }),
            Promise.resolve().then(function() {
                clear()
            })
        }
          , getLargeTime = function() {
            conf.page !== location.href ? conf.haveAjax && conf.haveFetch && loadTime && ajaxTime && fetchTime ? reportData(1) : conf.haveAjax && !conf.haveFetch && loadTime && ajaxTime ? reportData(1) : !conf.haveAjax && conf.haveFetch && loadTime && fetchTime ? reportData(1) : conf.haveAjax || conf.haveFetch || !loadTime || reportData(1) : conf.haveAjax && conf.haveFetch && ajaxTime && fetchTime ? reportData(2) : conf.haveAjax && !conf.haveFetch && ajaxTime ? reportData(2) : !conf.haveAjax && conf.haveFetch && fetchTime && reportData(2)
        }
          , perforPage = function() {
            if (window.performance) {
                var timing = performance.timing
                  , memoryInfo = performance.memory || {};
                conf.performance = {
                    dnst: timing.domainLookupEnd - timing.domainLookupStart || 0,
                    tcpt: timing.connectEnd - timing.connectStart || 0,
                    sslt: timing.connectEnd - timing.secureConnectionStart || 0,
                    ttfb: timing.responseStart - timing.requestStart || 0,
                    datadlt: timing.responseEnd - timing.responseStart || 0,
                    reqt: timing.responseEnd - timing.requestStart || 0,
                    andt: timing.domComplete - timing.domInteractive || 0,
                    tti: timing.domInteractive - timing.fetchStart || 0,
                    sourcest: timing.loadEventStart - timing.domContentLoadedEventEnd || 0,
                    wit: timing.responseStart - timing.navigationStart || 0,
                    domt: timing.domContentLoadedEventEnd - timing.navigationStart || 0,
                    lodt: timing.loadEventEnd - timing.navigationStart || 0,
                    radt: timing.fetchStart - timing.navigationStart || 0,
                    rdit: timing.redirectEnd - timing.redirectStart || 0,
                    uodt: timing.unloadEventEnd - timing.unloadEventStart || 0,
                    jsHeapSizeLimit: memoryInfo.jsHeapSizeLimit || 0,
                    totalJSHeapSize: memoryInfo.totalJSHeapSize || 1,
                    usedJSHeapSize: memoryInfo.usedJSHeapSize || 0,
                    memoryUsedPercent: (memoryInfo.usedJSHeapSize / memoryInfo.totalJSHeapSize * 100).toFixed(2) + "%"
                }
            }
        }
          , perforResource = function() {
            if (!window.performance || !window.performance.getEntries)
                return !1;
            var resource = performance.getEntriesByType("resource")
              , resourceList = [];
            if (!resource && !resource.length)
                return resourceList;
            resource.forEach(function(item) {
                if ((opt.isAjax || "xmlhttprequest" != item.initiatorType && "fetch" != item.initiatorType) && (opt.isResource || "xmlhttprequest" == item.initiatorType || "fetch" === item.initiatorType)) {
                    var json = {
                        name: item.name,
                        method: "GET",
                        type: item.initiatorType,
                        duration: item.duration.toFixed(2) || 0,
                        decodedBodySize: item.decodedBodySize || 0,
                        nextHopProtocol: item.nextHopProtocol
                    }
                      , name = item.name ? item.name.split("?")[0] : ""
                      , ajaxMsg = conf.ajaxMsg[name] || "";
                    ajaxMsg && (json.method = ajaxMsg.method || "GET",
                    json.type = ajaxMsg.type || json.type,
                    json.decodedBodySize = json.decodedBodySize || ajaxMsg.decodedBodySize),
                    resourceList.push(json)
                }
            }),
            conf.resourceList = resourceList
        }
          , fetArg = function(arg) {
            var result = {
                method: "GET",
                type: "fetchrequest"
            }
              , args = Array.prototype.slice.apply(arg);
            if (!args || !args.length)
                return result;
            try {
                1 === args.length ? "string" == typeof args[0] ? result.url = args[0] : "object" === _typeof(args[0]) && (result.url = args[0].url,
                result.method = args[0].method) : (result.url = args[0],
                result.method = args[1].method || "GET",
                result.type = args[1].type || "fetchrequest")
            } catch (err) {}
            return result
        }
          , ajaxResponse = function(xhr, type) {
            var defaults = Object.assign({}, errorInfo);
            defaults.t = (new Date).getTime(),
            defaults.n = "ajax",
            defaults.msg = xhr.statusText || "ajax response error",
            defaults.method = xhr.method || xhr.args.method;
            try {
                var res = xhr.xhr.responseText && JSON.parse(xhr.xhr.responseText)
            } catch (err) {}
            if (!(0 == res.c && 0 <= res.d)) {
                0 < res.code && res.message ? (defaults.code = res.code,
                defaults.message = res.message,
                defaults.zpData = res.zpData) : 0 < res.errcode && res.errmsg ? (defaults.code = res.errcode,
                defaults.message = res.errmsg,
                defaults.zpData = res.data) : defaults.res = res;
                var resourceUrl = xhr.args ? xhr.args.url : xhr.responseURL;
                defaults.data = {
                    resourceUrl: resourceUrl,
                    text: xhr.statusText,
                    status: xhr.status
                },
                conf.errorList.push(defaults),
                reportData(3, opt.action, "responseError")
            }
        }
          , getFetchTime = function(type) {
            conf.fetchNum += 1,
            conf.fetLength === conf.fetchNum && (conf.fetchNum = conf.fetLength = 0,
            fetchTime = (new Date).getTime() - beginTime,
            getLargeTime())
        }
          , getAjaxTime = function(type) {
            conf.loadNum += 1,
            conf.loadNum === conf.ajaxLength && (conf.ajaxLength = conf.loadNum = 0,
            ajaxTime = (new Date).getTime() - beginTime,
            getLargeTime())
        }
          , clearPerformance = function(type) {
            conf.haveAjax && conf.haveFetch && 0 == conf.ajaxLength && 0 == conf.fetLength || !conf.haveAjax && conf.haveFetch && 0 == conf.fetLength || conf.haveAjax && !conf.haveFetch && conf.ajaxLength,
            clear(1)
        }
          , ajax = function(options) {
            var params, xhr = null, isAsync = !0;
            (!1 === options.async && (isAsync = !1),
            xhr = window.XMLHttpRequest ? new XMLHttpRequest : new ActiveXObject("Microsoft.XMLHTTP"),
            "GET" == options.type.toUpperCase()) ? (options.data && (params = function(data) {
                var arr = [];
                for (var prop in data)
                    arr.push(prop + "=" + data[prop]);
                return arr.join("&")
            }(options.data)),
            params ? xhr.open(options.type, options.url + "?" + params, options.async) : xhr.open(options.type, options.url, options.async),
            xhr.send()) : "POST" == options.type.toUpperCase() && (xhr.open(options.type, options.url, isAsync),
            xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8"),
            xhr.setRequestHeader("report-source", "apmsdk-ajax-v" + window.APMSDKVERSION),
            options.data ? xhr.send(options.data) : xhr.send());
            xhr.onreadystatechange = function() {
                if (4 == xhr.readyState && 200 == xhr.status) {
                    var result = xhr.responseText;
                    "JSON" === options.dataType.toUpperCase() ? options.success(JSON.parse(result)) : options.success(result)
                }
            }
        }
          , clear = function(argument_0) {
            var type = 0 < arguments.length && void 0 !== argument_0 ? argument_0 : 0;
            window.performance && window.performance.clearResourceTimings && performance.clearResourceTimings(),
            conf.performance = {},
            conf.errorList = [],
            conf.preUrl = "",
            conf.resourceList = [],
            conf.page = 0 === type ? location.href : "",
            conf.haveAjax = !1,
            conf.haveFetch = !1,
            conf.ajaxMsg = {},
            ERRORLIST = [],
            ADDDATA = {},
            fetchTime = ajaxTime = 0
        }
          , opt = {
            userIdUrl: "",
            domain: (window.location.origin.endsWith(".zhipin.com") ? "https://apm-fe.zhipin.com" : "https://apm-fe-qa.weizhipin.com") + "/wapi/zpApm/actionLog/fe/common.json",
            appKey: "7O9U1uHCgZ8r0DK7",
            action: "action_js_monitor",
            outtime: 0,
            filterUrl: [],
            isPerformance: !0,
            isAjax: !0,
            isFetch: !0,
            isResource: !0,
            isKAjs: !0,
            isError: !0,
            isResponseCode: !0,
            add: {}
        };
        (opt = Object.assign(opt, option)).filterUrl = opt.filterUrl.concat(["/api/v1/report/web", "livereload.js?snipver=1", "/sockjs-node/info"]);
        var conf = {
            resourceList: [],
            performance: {},
            errorList: [],
            fetchNum: 0,
            loadNum: 0,
            ajaxLength: 0,
            fetLength: 0,
            ajaxMsg: {},
            goingType: "",
            haveAjax: !1,
            haveFetch: !1,
            preUrl: document.referrer && document.referrer !== location.href ? document.referrer : "",
            page: ""
        }
          , errorInfo = {
            t: "",
            n: "js",
            msg: "",
            data: {}
        }
          , beginTime = (new Date).getTime()
          , loadTime = 0
          , ajaxTime = 0
          , fetchTime = 0;
        opt.isError && function() {
            window.addEventListener("error", function(e) {
                var defaults = Object.assign({}, errorInfo);
                defaults.n = "resource",
                defaults.t = (new Date).getTime(),
                defaults.msg = e.target.localName + " is load error",
                defaults.data = {
                    target: e.target.localName,
                    type: e.type,
                    resourceUrl: e.target.href || e.target.currentSrc || e.target.src || "unknown path: " + e.target.className
                },
                e.target != window && conf.errorList.push(defaults)
            }, !0),
            window.onerror = function(msg, url, line, col, error) {
                var defaults = Object.assign({}, errorInfo);
                if ("Script error." == msg && !url)
                    return !0;
                setTimeout(function() {
                    if (col = col || window.event && window.event.errorCharacter || 0,
                    error && error.stack)
                        defaults.msg = error.stack.toString();
                    else if (arguments.callee) {
                        for (var ext = [], f = arguments.callee.caller, c = 3; f && 0 < --c && (ext.push(f.toString()),
                        f !== f.caller); )
                            f = f.caller;
                        ext = ext.join(","),
                        defaults.msg = ext
                    } else
                        defaults.msg = msg || "window.onerror uncaught errorInfo";
                    defaults.data = {
                        resourceUrl: url,
                        line: line,
                        col: col
                    },
                    defaults.t = (new Date).getTime(),
                    conf.errorList.push(defaults),
                    conf.haveAjax || reportData(3, opt.action, "jsError")
                }, 0)
            }
            ,
            window.addEventListener("unhandledrejection", function(e) {
                var resourceUrl, col, line, error = e && e.reason, message = error.message || "", stack = error.stack || "", errs = stack.match(/\(?(http|<anonymous>).+\)?/);
                errs && errs.length && (errs = (errs = (errs = errs[0]).replace(/\w.+[js|html]/g, function($1) {
                    return resourceUrl = $1,
                    ""
                })).split(":")) && 1 < errs.length && (line = parseInt(errs[1] || 0),
                col = parseInt(errs[2] || 0));
                var defaults = Object.assign({}, errorInfo);
                defaults.msg = message,
                defaults.type = e.type,
                defaults.stack = stack,
                defaults.t = (new Date).getTime(),
                defaults.data = {
                    resourceUrl: resourceUrl,
                    line: line,
                    col: col
                },
                conf.errorList.push(defaults),
                conf.page !== location.href || conf.haveAjax || reportData(3, opt.action, "promiseError")
            }),
            window.addEventListener("rejectionhandled", function(event) {}, !1);
            var oldError = console.error;
            console.error = function(e) {
                var defaults = Object.assign({}, errorInfo);
                return setTimeout(function() {
                    defaults.msg = e,
                    defaults.method = "GET",
                    defaults.t = (new Date).getTime(),
                    defaults.data = {
                        resourceUrl: location.href
                    },
                    conf.errorList.push(defaults),
                    conf.page !== location.href || conf.haveAjax || reportData(3, opt.action, "diyError")
                }, 0),
                oldError.apply(console, arguments)
            }
        }();
        var timer = null;
        window.addEventListener("load", function() {
            loadTime = (new Date).getTime() - beginTime,
            getLargeTime(),
            timer = setTimeout(function() {
                opt.isKAjs && function() {
                    for (var scriptsEles = document.getElementsByTagName("script"), iskajs = !1, i = 0; i < scriptsEles.length; i++)
                        if (scriptsEles[i].src && scriptsEles[i].getAttribute("src").includes("ka.")) {
                            iskajs = !0;
                            break
                        }
                    iskajs || reportData(3, opt.action, "notFindKAjs"),
                    clearTimeout(timer)
                }()
            }, 3e3)
        }, !1),
        opt.isFetch && opt.isError && function() {
            if (window.fetch) {
                var _fetch = fetch;
                window.fetch = function() {
                    var result = fetArg(arguments);
                    if ("report-data" !== result.type) {
                        clearPerformance();
                        var url = result.url ? result.url.split("?")[0] : "";
                        conf.ajaxMsg[url] = result,
                        conf.fetLength = conf.fetLength + 1,
                        conf.haveFetch = !0
                    }
                    return _fetch.apply(this, arguments).then(function(res) {
                        if ("report-data" === result.type)
                            return res;
                        try {
                            var _url = res.url ? res.url.split("?")[0] : "";
                            res.clone().text().then(function(data) {
                                conf.ajaxMsg[_url] && (conf.ajaxMsg[_url].decodedBodySize = data.length)
                            })
                        } catch (e) {}
                        return getFetchTime("success"),
                        res
                    }).catch(function(err) {
                        if ("report-data" !== result.type) {
                            getFetchTime("error");
                            var defaults = Object.assign({}, errorInfo);
                            return defaults.t = (new Date).getTime(),
                            defaults.n = "fetch",
                            defaults.msg = "fetch request error",
                            defaults.method = result.method,
                            defaults.data = {
                                resourceUrl: result.url,
                                text: err.stack || err,
                                status: 0
                            },
                            conf.errorList.push(defaults),
                            err
                        }
                    })
                }
            }
        }(),
        opt.isAjax && opt.isError && (proxy = {
            onreadystatechange: function(xhr) {
                4 === xhr.readyState && setTimeout(function() {
                    if ("load" !== conf.goingType) {
                        conf.goingType = "readychange",
                        getAjaxTime();
                        var responseURL = xhr.xhr.responseURL ? xhr.xhr.responseURL.split("?")[0] : "";
                        if (conf.ajaxMsg[responseURL])
                            try {
                                xhr.xhr.response instanceof Blob ? conf.ajaxMsg[responseURL].decodedBodySize = xhr.xhr.response.size : conf.ajaxMsg[responseURL].decodedBodySize = xhr.xhr.responseText.length
                            } catch (err) {}
                        try {
                            var res = "arraybuffer" != xhr.xhr.responseType && xhr.xhr.responseText && JSON.parse(xhr.xhr.responseText);
                            opt.isResponseCode && 200 == xhr.xhr.status && res && 0 != res.code && ajaxResponse(xhr),
                            opt.isResponseCode && 200 == xhr.xhr.status && res && res.errcode && 0 != res.errcode && ajaxResponse(xhr)
                        } catch (err) {}
                        (xhr.status < 200 || 0 == xhr.status || 400 <= xhr.status) && (xhr.method = xhr.args && xhr.args.method,
                        ajaxResponse(xhr))
                    }
                }, 500)
            },
            onerror: function(xhr) {
                getAjaxTime(),
                xhr.args && (xhr.method = xhr.args.method,
                xhr.responseURL = xhr.args.url,
                xhr.statusText = "ajax request error",
                conf.ajaxMsg[xhr.responseURL] && getAjaxTime()),
                ajaxResponse(xhr)
            },
            onload: function(xhr) {
                if (4 === xhr.readyState) {
                    if ("readychange" === conf.goingType)
                        return;
                    conf.goingType = "load",
                    getAjaxTime();
                    var responseURL = xhr.xhr.responseURL ? xhr.xhr.responseURL.split("?")[0] : "";
                    if (conf.ajaxMsg[responseURL])
                        try {
                            xhr.xhr.response instanceof Blob ? conf.ajaxMsg[responseURL].decodedBodySize = xhr.xhr.response.size : conf.ajaxMsg[responseURL].decodedBodySize = xhr.xhr.responseText.length
                        } catch (err) {}
                    try {
                        var res = "arraybuffer" != xhr.xhr.responseType && xhr.xhr.responseText && JSON.parse(xhr.xhr.responseText);
                        opt.isResponseCode && 200 == xhr.xhr.status && res && 0 != res.code && ajaxResponse(xhr),
                        opt.isResponseCode && 200 == xhr.xhr.status && res && res.errcode && 0 != res.errcode && ajaxResponse(xhr)
                    } catch (err) {}
                    (xhr.status < 200 || 0 == xhr.status || 400 <= xhr.status) && (xhr.method = xhr.args && xhr.args.method,
                    ajaxResponse(xhr))
                }
            },
            onloadend: function(xhr) {
                this.onreadystatechange(xhr)
            },
            open: function(arg, xhr) {
                if (opt.filterUrl && opt.filterUrl.length) {
                    var begin = !1;
                    if (opt.filterUrl.forEach(function(item) {
                        -1 != arg[1].indexOf(item) && (begin = !0)
                    }),
                    begin)
                        return
                }
                var result = {
                    url: arg[1].split("?")[0],
                    method: arg[0] || "GET",
                    type: "xmlhttprequest"
                };
                this.args = result,
                clearPerformance(),
                conf.ajaxMsg[result.url] = result,
                conf.ajaxLength = conf.ajaxLength + 1,
                conf.haveAjax = !0
            }
        },
        window._ahrealxhr = window._ahrealxhr || XMLHttpRequest,
        XMLHttpRequest = function() {
            for (var attr in this.xhr = new window._ahrealxhr,
            this.xhr) {
                var type = "";
                try {
                    type = _typeof(this.xhr[attr])
                } catch (e) {}
                "function" === type ? this[attr] = hookfun(attr) : Object.defineProperty(this, attr, {
                    get: getFactory(attr),
                    set: setFactory(attr)
                })
            }
        }
        ,
        window._ahrealxhr),
        customReport = reportData
    } catch (err) {}
    function getFactory(attr) {
        return function() {
            var v = this.hasOwnProperty(attr + "_") ? this[attr + "_"] : this.xhr[attr]
              , attrGetterHook = (proxy[attr] || {}).getter;
            return attrGetterHook && attrGetterHook(v, this) || v
        }
    }
    function setFactory(attr) {
        return function(v) {
            var xhr = this.xhr
              , that = this
              , hook = proxy[attr];
            if ("function" == typeof hook)
                xhr[attr] = function() {
                    proxy[attr](that) || v.apply(xhr, arguments)
                }
                ;
            else {
                var attrSetterHook = (hook || {}).setter;
                v = attrSetterHook && attrSetterHook(v, that) || v;
                try {
                    xhr[attr] = v
                } catch (e) {
                    this[attr + "_"] = v
                }
            }
        }
    }
    function hookfun(fun) {
        return function() {
            var args = [].slice.call(arguments);
            if (!proxy[fun] || !proxy[fun].call(this, args, this.xhr))
                return this.xhr[fun].apply(this.xhr, args)
        }
    }
    var proxy
}
"function" == typeof require && "object" === ("undefined" == typeof exports ? "undefined" : _typeof(exports)) && "object" === ("undefined" == typeof module ? "undefined" : _typeof(module)) ? module.exports = performanceReport : window.performanceReport = performanceReport,
window.ERRORLIST = [],
window.ADDDATA = {},
window.APMSDKVERSION = "1.12",
performanceReport.addError = function(err) {
    err = {
        msg: err.msg,
        n: "js",
        data: {
            col: err.col,
            line: err.line,
            resourceUrl: err.resourceUrl
        }
    },
    ERRORLIST.push(err)
}
,
performanceReport.addData = function(fn) {
    fn && fn(ADDDATA)
}
;
