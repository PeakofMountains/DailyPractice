// 设置使JS代码在元素创建完毕后再执行
window.addEventListener('load', function () {
    var goods = this.document.querySelector('.goods');
    var photo = this.document.querySelector('.photo');
    var mask = this.document.querySelector('.mask');
    var magnifier = this.document.querySelector('.magnifier');
    var magnifierImage = this.document.querySelector('.magnifierImage');

    // 鼠标经过图片时显示mask和magnifier
    photo.addEventListener('mouseover', function () {
        mask.style.display = 'block';
        magnifier.style.display = 'block';
    })
    // 鼠标移出图片时隐藏mask和magnifier
    photo.addEventListener('mouseout', function () {
        mask.style.display = 'none';
        magnifier.style.display = 'none';
    })

    photo.addEventListener('mousemove', function (e) {
        // 计算mask应移动的距离
        var x = e.pageX - goods.offsetLeft;
        var y = e.pageY - goods.offsetTop;
        // maskMaxX和maskMaxY分别是mask在图片内横向和纵向移动的最大距离
        var maskMaxX = (photo.offsetWidth - mask.offsetWidth / 2);
        var maskMaxY = (photo.offsetHeight - mask.offsetHeight / 2);
        // 设置使mask不能超出图片范围
        if (x < (mask.offsetWidth / 2)) {
            x = mask.offsetWidth / 2;
        }
        else if (x > maskMaxX) {
            x = photo.offsetWidth - mask.offsetWidth / 2;
        }
        if (y < (mask.offsetHeight / 2)) {
            y = mask.offsetHeight / 2;
        }
        else if (y > maskMaxY) {
            y = photo.offsetHeight - mask.offsetHeight / 2;
        }
        // 设置mask移动的距离
        mask.style.left = x + 'px';
        mask.style.top = y + 'px';
        // 计算放大图片在放大盒子内的最大移动距离
        var magnifierMaxX = (magnifierImage.offsetWidth - magnifier.offsetWidth);
        var magnifierMaxY = (magnifierImage.offsetHeight - magnifier.offsetHeight);
        // 两个mask和放大图片magnifierImage的最大移动距离是成比例的，由此算出放大图片应该移动的距离
        magnifierImage.style.left = -x * magnifierMaxX / maskMaxX + 'px';
        magnifierImage.style.top = -y * magnifierMaxY / maskMaxY + 'px';


    })

})