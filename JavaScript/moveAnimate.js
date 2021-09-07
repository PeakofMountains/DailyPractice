function moveAnimate(obj, position, callback) {
    // 首先进行清除定时器的操作，防止对象本身带着定时器，多个定时器引起bug
    clearInterval(obj.timer);
    obj.timer = setInterval(function () {
        var step = (position - obj.offsetLeft) / 10;
        step = step > 0 ? Math.ceil(step) : Math.floor(step);
        // 缓冲动画的步长不是固定不变的，是根据目的点与当前位置进行计算，是动态改变的
        obj.style.left = obj.offsetLeft + step + 'px';
        // 移动到指定位置停止
        if (obj.offsetLeft == position) {
            clearInterval(obj.timer);
            // 如果回调函数存在，定时器结束后执行回调函数
            if (callback) {
                callback();
            }
        }
    }, 15)
}