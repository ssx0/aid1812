$(function (){
	//全选和取消全选
	var checkall = false;
	$("#checkall").click(function (){
		checkall = !checkall;
		if(checkall){
			$(this).attr("src","../images/cart/product_true.png");
			$(".choose").attr("src","../images/cart/product_true.png").attr("check","true");
			console.log($(".choose").attr("check"));
		}else{
			$(this).attr("src","../images/cart/product_normal.png");
			$(".choose").attr("src","../images/cart/product_normal.png").removeAttr("check");
		}
		sum();
	
	});
	//反选
	$(".choose").click(function (){
		//当前为选中状态，那就取消选中
		if($(this).attr("check")){
			$(this).removeAttr("check");
			$(this).attr("src","../images/cart/product_normal.png");
		}else{//当前未选中，点击选中
			$(this).attr("check","true").attr("src","../images/cart/product_true.png");
		}
		//反选
		//被选中的商品数量跟总共的商品数量相等 -》 全选
		if($("img[check=true]").length == $(".choose").length){
			$("#checkall").attr("src","../images/cart/product_true.png");
			checkall = true;
		}else{
			$("#checkall").attr("src","../images/cart/product_normal.png");
			checkall = false;
		}
		sum();
	
	});
	//数量操作
	$(".decrement").click(function (){
		var count = $(this).next().val();
		if(count > 1){
			count--;
			$(this).next().val(count);
		}
		//价格联动
		//￥388.00
		var priceStr = $(this).parent().prev().find("span").eq(1).html();
		//388.00
		var price = priceStr.substring(1);
		$(this).parent().next().html("￥"+count*price);
		sum();

	});
	$(".increment").click(function (){
		var count = $(this).prev().val();
		$(this).prev().val(++count);
		//价格联动
		//￥388.00
		var priceStr = $(this).parent().prev().find("span").eq(1).html();
		//388.00
		var price = priceStr.substring(1);
		$(this).parent().next().html("￥"+count*price);
		sum();
	})
	//移除
	$(".action a").click(function (){
		$(this).parents(".item").remove();
		sum();
	});
	//总价和总数量
	function sum(){
		var totalPrice = 0;
		var totalNum = 0;
		//遍历所有被选中商品，获取其数量和总价
		$("img[check=true]").each(function (){
			//获取当前商品的数量
			var num = Number($(this).parent().siblings(".count").find("input").val());
			var priceStr = $(this).parent().siblings(".sum").html();
			//获取当前商品的总价
			var price = Number(priceStr.substring(1));
			//做累加
			totalPrice += price;
			totalNum += num;
		});
		//修改标签
		$(".total-num").html(totalNum);
		$(".total-price").html("￥"+totalPrice);
	}
	

})