window.addEventListener('load', function () {
    let wrapper = document.getElementById("wrapper");
    let month = document.getElementById("month");
    let date = document.getElementById("date");
    let hour = document.getElementById("hour");
    let minute = document.getElementById("minute");
    let second = document.getElementById("second");
    let img = this.document.querySelector('.background img');

    /*
    * 初始化月份函数
    * */
    let initMonth = function () {
        for (let i = 1; i <= 12; i++) {
            // 依次创建12个月份的小盒子
            let span = document.createElement("span");
            span.innerHTML = i + " 月";
            month.appendChild(span);
        }
    };

    // 初始化日期，小时，分钟，秒
    let initDate = function () {
        for (let i = 1; i <= 31; i++) {
            let span = document.createElement("span");
            span.innerHTML = i + "日";
            date.appendChild(span);
        }
    };
    let initHour = function () {
        for (let i = 0; i < 24; i++) {
            let span = document.createElement("span");
            span.innerHTML = i < 10 ? ('0' + i + '时') : (i + '时');
            hour.appendChild(span);
        }
    };
    let initMinute = function () {
        for (let i = 0; i < 60; i++) {
            let span = document.createElement("span");
            span.innerHTML = i < 10 ? ('0' + i + '分') : (i + '分');
            minute.appendChild(span);
        }
    };
    let initSecond = function () {
        for (let i = 0; i < 60; i++) {
            let span = document.createElement("span");
            span.innerHTML = i < 10 ? ('0' + i + '秒') : (i + '秒');
            second.appendChild(span);
        }
    };

    // 当前时间文字样式切换函数
    let changeTime = function (tag) {
        let tagParent = tag.parentNode;
        for (var i = 0; i < tagParent.children.length; i++) {
            tagParent.children[i].className = '';
        }
        // 当前标签添加样式类
        tag.className = "on";
    };

    //  初始化日历函数
    let init = function () {
        initMonth(); // 初始化月份
        initDate(); // 初始化日期
        initHour(); // 小时
        initMinute();
        initSecond();
    };

    /*
    * 展示当前时间
    * 参数：mydate 时间对象
    * */
    let getNowTime = function (mydate) {
        // 得到系统当前时间
        let Month = mydate.getMonth();
        let Date = mydate.getDate();
        let Hour = mydate.getHours();
        let Minute = mydate.getMinutes();
        let Second = mydate.getSeconds();
        // 当前时间文字样式切换函数
        changeTime(month.children[Month]);
        changeTime(date.children[Date - 1]);
        changeTime(hour.children[Hour]);
        changeTime(minute.children[Minute]);
        changeTime(second.children[Second]);

    };

    // 展示时间圆圈函数
    // tag：目标
    // dis：圆圈半径
    let textRound = function (tag, dis) {
        let span = tag.children;
        for (let i = 0; i < span.length; i++) {
            // 计算每一个span需要转动的角度
            span[i].style.transform = "rotate(" + (360 / span.length) * i + "deg)  translateX(" + dis + "px)";
        }
    };

    // 旋转指定“圆圈”指定度数,保持当前时间显示在最右端
    let rotateTag = function (tag, deg) {
        tag.style.transform = "rotate(" + deg + "deg)";
    };

    let main = function () {
        init(); // 初始化日历
        setInterval(function () {
            let mydate = new Date();
            getNowTime(mydate); // 展示当前时间
        }, 1000);

        textRound(month, 60);
        textRound(date, 120);
        textRound(hour, 180);
        textRound(minute, 240);
        textRound(second, 300);
        let clockTimer = setInterval(function () {
            let mydate = new Date();
            // 恢复当前起始时间
            rotateTag(month, -360 / 12 * mydate.getMonth());
            rotateTag(date, -360 / 31 * (mydate.getDate() - 1));
            rotateTag(hour, -360 / 24 * mydate.getHours());
            rotateTag(minute, -360 / 60 * mydate.getMinutes());
            rotateTag(second, -360 / 60 * mydate.getSeconds());
        }, 1000);
        let backgroundTimer = setInterval(function () {
            let mydate = new Date();

            img.src = 'images/' + mydate.getSeconds() % 5 + '.png';
            // console.log(second);
        }, 8000)
    };
    main();

})