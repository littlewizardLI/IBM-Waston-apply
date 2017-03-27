$(function(){
  var list = $("#list");
  var width = parseInt(list.css("width")) / 6;
  var prev = $("#prev");
  var next = $("#next");
  var span = $("#buttons span");
  var index = 1;
  var timer = null;
  var interval = 3000;

  list.css("left",-width);//第一张为4.jpg，left=0；减去width，偏移到1.jpg
  
  function animate(offset){ //过渡
  	var newLeft = parseInt(list.css("left")) + offset;
  	list.animate({"left": newLeft + "px"},function(){
      if(newLeft > 0){
        list.css("left", -width * 4);
      }//左击超出，回归第四张图
      if(newLeft  < -width * 4){
        list.css("left", -width);
      }//右击超出，回归第一张图
  	});
  }

  function showButtons(){
    span.each(function(){
      $(this).attr("class", "");
    });
    $("#buttons span").eq(index - 1).addClass("on");
  }

  prev.on("click",function(){
    if(list.is(":animated")) return;
    if(index == 1){
      index = 4;
    }else{
      index -= 1;
    }
    animate(width);
    showButtons();
  });

  next.on("click",function(){
  	if(list.is(":animated")) return;
    if(index == 4){
      index = 1;
    }else{
      index += 1;
    }
    animate(-width);
    showButtons();
  });

  function autoplay(){
    timer = setTimeout(function(){
      next.trigger("click");
      autoplay();
    },interval);
  }

  function stop(){
    clearInterval(timer);
  }

  list.on("mouseover", function(){
    stop();
  });

  list.on("mouseout",function(){
    autoplay();
  });

  span.each(function(){
    $(this).on("click",function(){
      if(list.is(":animated") || $(this).attr("class") == "on") return;
      var myIndex = $(this).attr("index");
      var offset = (myIndex - index) * -width;
      index = myIndex;
      
      animate(offset);
      showButtons();
    })
  });

  autoplay();

});