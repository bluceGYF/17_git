// JavaScript Document
$(function(){
	//.InPorNav li
	$(".InPorNav li").hover(function(){
		$(this).addClass("inProNavStyle");
		$(this).children(".chilInPorNav").stop(true,true).show();
		},function(){
		$(this).removeClass("inProNavStyle");
		$(this).children(".chilInPorNav").stop(true,true).hide();})
	//rdList
	$(".rdList li:first").addClass("rdListStyle");
	$(".rdProBox:first").show();
	$(".rdList li").click(function(){
		$(this).addClass("rdListStyle").siblings("li").removeClass("rdListStyle");
		var index=$(this).index();
		$(".rdProBox").eq(index).show().siblings(".rdProBox").hide();
		})	
	//.rdPro dl
	$(".rdPro dl").hover(function(){
		$(this).addClass("rddlstyle");
		$(this).stop(true,true).animate({
			opacity:"0.7"
			})
		},function(){$(this).removeClass("rddlstyle");$(this).stop(true,true).animate({
			opacity:"1"
			})})
	//.upd,.add
	$(".upd,.add,.vipUp").click(function(){
		$(".address").stop(true,true).slideDown();
		})
	//flList
	$("#floor1 .frProList:first").show();
	$("#floor2 .frProList:first").show();
	$("#floor3 .frProList:first").show();
	$(".flList li:first").addClass("flListStyle")
	$("#floor1 .flList li").click(function(){
		$(this).addClass("flListStyle").siblings("li").removeClass("flListStyle");
		var index2=$(this).index();
		$("#floor1 .frProList").eq(index2).show().siblings(".frProList").hide();
		})	
	$("#floor2 .flList li").click(function(){
		$(this).addClass("flListStyle").siblings("li").removeClass("flListStyle");
		var index2=$(this).index();
		$("#floor2 .frProList").eq(index2).show().siblings(".frProList").hide();
		})	
	$("#floor3 .flList li").click(function(){
		$(this).addClass("flListStyle").siblings("li").removeClass("flListStyle");
		var index2=$(this).index();
		$("#floor3 .frProList").eq(index2).show().siblings(".frProList").hide();
		})	
	//.floorRight dl
	$(".floorRight .frProList dl,.contRight .frProList dl").hover(function(){
		$(this).stop(true,true).addClass("frListDlstyle");
		$(this).animate({
		    opacity:"0.8",
			left:"-4px"
			})
		},function(){
	    $(this).removeClass("frListDlstyle");
		$(this).stop(true,true).animate({
		    opacity:"1",
			left:"0px"
			})
			})
	//返回首页代码
 var bodyWidth2=$($(window)).height()-200;	
$(window).scroll(function(){
	if($(this).scrollTop() > bodyWidth2)
	{
		$('.backTop').fadeIn();
	}
	else{
		$('.backTop').fadeOut();
	}
})
   //.Title 下拉产品菜单
   $(".Title").hover(function(){
	   $(this).children(".InPorNav").show();
	   },function(){$(this).children(".InPorNav").hide();})
   //.leftPorNav
   $(".leftPorNav li").hover(function(){
	   $(this).children(".chilInPorNav").show();
	   },function(){
		   $(this).children(".chilInPorNav").hide();
		   })  
	//选择支付方式 
	$(".zhiList li:first").addClass("zhistyle");
	$(".zhifufangshi:first").show();
	$(".zhiList li").click(function(){
		$(this).addClass("zhistyle").siblings("li").removeClass("zhistyle");
		var zhi=$(this).index();
		$(".zhifufangshi").eq(zhi).show().siblings(".zhifufangshi").hide();
		})
	//.rongliang li
	$(".rongliang li").click(function(){
		$(this).addClass("rongStyle").siblings("li").removeClass("rongStyle");
		})
	//.fangLists:first
	$(".fangList:first").show();
	$(".fangyuan li").click(function(){
		$(this).addClass("fangyuanstyle").siblings("li").removeClass("fangyuanstyle");
		var fangyuan=$(this).index();
		$(".fangList").eq(fangyuan).show().siblings(".fangList").hide();
		})	
	//vipNav
	$(".vipNav dt").click(function(){
		$(this).addClass("vipNavStyle").siblings("dt").removeClass("vipNavStyle");
		$(this).next("dd").show().siblings("dd").hide();
		})
	//登录验证
	// $('.submit').click(function(event){
     //            var name = $('.name').val();
	// 			var pwd = $('.pwd').val();
	//
     //            var namelen = name.length;
	// 			var pwdlen = pwd.length;
     //            if(namelen < 6){
     //                    alert("用户名不能小于六位，请重新输入！")
	// 				    return false;
     //                    }
	//
	// 			if(pwdlen < 6){
     //                    alert("你输入的密码不正确，请重新输入！")
	// 				    return false;
     //                    }
	//
     //            });
	//会员中心修改密码验证
	$(".vipSub").click(function(){
		var pwd1=$(".vipPwd1").val();
	    var pwd2=$(".vipPwd2").val();
		if(pwd1!==pwd2||pwd1<1){
			alert("两次输入的密码不一样,请重新输入");
			$(".vipPwd1,.vipPwd2").val("");
			}
			else{
				alert("恭喜您，修改成功！");
				$(".vipPwd1,.vipPwd2").val("");
				}
		})
	})
	
//banner	
	/*! jQuery.kinMaxShow v1.0 | mr.kin@foxmail.com */
eval((function(a,b){return a.replace(/\w+/g, function(ss){ return b[parseInt(ss, 36)]; }); })("(0($){\r$.1.2 = 0(3){\r4 5 = {\r6:7,\r8:9,\ra:b,\rc:\'d\',\re:\'f f\',\rg:{\rh:\'i\',\rj:k,\rl:{m:\'n\',6:\'n\',o:\'n\',p:\'q\',r:\'q\',s:\'q\',t:\"#u\",v:\"w x #y\",z:\"#10\",11:\'f\',12:\'13\',14:\"15\",16:\'17\'},\r18:{t:\"#19\",v:\"w x #1a\",z:\"#1b\"}\r},\r1c:0(1d,1e){}\r};\r1f = 1g.1h(1i,{},5,3);\r4 1j = {};\r1j.1k = $(1l).1k;\r1m($(1l).1n>1o){\r$.1p(\'2 1p[1q 1r 1s 1t 1u]\');\r1v k;\r}\r1j.1w = 1l;\r1j.1d = 1x;\r1j.1y = 1x;\r1j.1z = $(1j.1w).20(\'21\').1z();\r1j.22 = \'23\';\r1j.24 = {};\r1j.1 = {};\r1j.25 = 0(){\r$(1j.1w).26({m:\'27%\',6:1f.6,28:\'29\',2a:\'2b\'}).20(\'21\').2c(1j.22+\'2d\').2e();\r1j.2f();\r};\r1j.2f = 0(){\r1j.2g();\r1j.2h();\r1j.2i();\r};\r1j.2g = 0(){\r1j.24.2j = 2k 2l();\r$(1j.1w).20(\'21\').2m(0(){\r1j.24.2j.2n($(1l).2o(\'2p\').2q(\'2r\'));\r})\r};\r1j.2h = 0(){\r$(1j.1w).20(\'21\').2s(\'<21 2t=\"\'+1j.22+\'2u\"><\/21>\');\r$(\'.\'+1j.22+\'2d\',1j.1w).2m(0() {\r4 2v = $(1l).20(\'2v\');\r1m(2v.1n){\r4 2w = 2v.20(\'2p\').2q(\'2x\');\r2v.20(\'2p\').2y();\r}2z{\r4 2w = $(1l).20(\'2p\').2q(\'2x\');\r$(1l).20(\'2p\').2y();\r}\r$(1l).26({t:\'30(\'+2w+\') 31-32 \'+1f.e,\'33-1d\':1x});\r});\r$(\'.\'+1j.22+\'2d\',1j.1w).34(1x).26(\'33-1d\',\'1o\');\r1m(1f.g.l.35!=\'36\'){\r4 37 = \'\';\r38(39=1o;39<=1j.1z;39++){\r1m(1f.g.j){\r37+=\'<3a>\'+39+\'<\/3a>\';\r}2z{\r37+=\'<3a> <\/3a>\';\r}\r}\r$(1j.1w).3b(\'<3c 2t=\"\'+1j.22+\'g\">\'+37+\'<\/3c>\');\r$(\'.\'+1j.22+\'g 3a\',1j.1w).34(1x).2c(\'18\');\r}\r1j.3d();\r$(\'.\'+1j.22+\'2d:3e(1x)\',1j.1w).26(\'33-1d\',1x).26({3f:1x});\r$(\'.\'+1j.22+\'2d\',1j.1w).3g();\r$(1j.1w).26({28:\'3h\',3i:\'3h\',35:\'3j\'});\r};\r1j.3d = 0(){\r4 3k = \'<3l 3m=\"3n\/26\">\';\r3k+= 1j.1k+\' *{ 3o:1x;3p:1x;} \';\r3k+= 1j.1k+\' .\'+1j.22+\'2u{m:27%;6:\'+3q(1f.6)+\'3r;2a:2b;33-1d:1o;} \';\r3k+= 1j.1k+\' .\'+1j.22+\'2u .\'+1j.22+\'2d{m:27%;6:\'+3q(1f.6)+\'3r;2a:3s;28:29;} \';\r3k+= 1j.1k+\' .\'+1j.22+\'2u .\'+1j.22+\'2d 2v{m:27%;6:\'+3q(1f.6)+\'3r;35:3j;3n-3t:36;3p:1x;3o:1x;t:3u;3n-3v:1x;3w:36;2e-18:3x(1l.3y=1i);} \';\r1m(1f.g.l.35!=\'36\'){\r3k+= 1j.1k+\' .\'+1j.22+\'g{\'+1j.1.3z(1f.g.l,[\'40\',\'p\',\'r\',\'17\'],1i)+\';2a:3s;41-3l:36;33-1d:42;}\';\r3k+= 1j.1k+\' .\'+1j.22+\'g 3a{\'+1j.1.3z(1f.g.l,[\'40\',\'p\',\'r\',\'17\'])+\';43:44;-45-3n-1z-46:36;}\';\r3k+= 1j.1k+\' .\'+1j.22+\'g 3a.18{\'+1j.1.3z(1f.g.18,[\'40\',\'p\',\'r\',\'17\'])+\';43:47;}\';\r}\r3k+= \'<\/3l>\';\r$(1j.1w).48(3k);\r}\r1j.2i = 0(){\r1f.1c.49($(\'.\'+1j.22+\'2d:34(\'+1j.1d+\')\',1j.1w),1j.1d,\'4a\');\r4 4b;\r$(\'.\'+1j.22+\'g\',1j.1w).4c(\'3a\',1f.g.h,0(){\r4d = 1l;\r0 4e(){\r1j.1d = $(4d).1d();\r1j.4f();\r}\r1m(1f.g.h==\'4g\'){\r4b = 4h(4e,4i);\r}2z{\r4e();\r}\r})\r1m(1f.g.h==\'4g\'){\r$(\'.\'+1j.22+\'g\',1j.1w).4c(\'3a\',\'4j\',0(){\r4k(4b);\r})\r}\r1j.1d = 1o;\r1j.1y = 1x;\r1j.24.4l = 4m(1j.4f,1f.8*b+1f.a);\r};\r1j.4f = 0(){\r1f.1c.49($(\'.\'+1j.22+\'2d:34(\'+(1j.1y)+\')\',1j.1w),1j.1y,\'4n\');\r4o(1j.24.4l);\r1m(1f.g.l.35!=\'36\'){\r$(\'3c.\'+1j.22+\'g 3a\',1j.1w).4p(\'18\');\r$(\'3c.\'+1j.22+\'g 3a\',1j.1w).34(1j.1d).2c(\'18\');\r}\r$(\'.\'+1j.22+\'2d:4q\',1j.1w).4r(1i,k);\r$(\'.\'+1j.22+\'2d\',1j.1w).26(\'33-1d\',1x);\r$(\'.\'+1j.22+\'2d\',1j.1w).34(1j.1d).26({3f:1x,\'33-1d\':1o});\r$(\'.\'+1j.22+\'2d\',1j.1w).34(1j.1d).4s({3f:1o},{4t:1f.a,c:1f.c,4u:0(){\r$(\'.\'+1j.22+\'2u .\'+1j.22+\'2d:4v(:34(\'+1j.1d+\'))\',1j.1w).26({3f:1x});\r1f.1c.49($(\'.\'+1j.22+\'2d:34(\'+1j.1d+\')\',1j.1w),1j.1d,\'4a\');\r1j.24.4l = 4m(1j.4f,1f.8*b+1f.a);\r1j.1y = 1j.1d;\r1m(1j.1d==1j.1z-1o){\r1j.1d=1x;\r}2z{\r1j.1d++;\r}\r}\r});\r};\r1j.4w = 0(){\r1j.25();\r};\r1j.1.3z = 0(4x,4y,4z){\r4z = 4z?1i:k;\r4 50 = 51.52.53(\"54\")!=-1o;\r4 3l = \'\';\r1m(4z){\r38 (4 55 56 4x){\r1m($.57(55,4y)!=-1o){\r58 = 55.59(\/([5a-5b])\/,5c);\r1m(58==\'3f\' && 50){\r3l +=\"5d:5e(3f=\"+(4x[55]*27)+\");\";\r}2z{\r3l +=58+\":\"+4x[55]+\";\";\r}\r}\r};\r}2z{\r38 (4 55 56 4x){\r1m($.5f(4y)){\r1m($.57(55,4y)==-1o){\r58 = 55.59(\/([5a-5b])\/,5c);\r1m(58==\'3f\' && 50){\r3l +=\"5d:5e(3f=\"+(4x[55]*27)+\");\";\r}2z{\r3l +=58+\":\"+4x[55]+\";\";\r}\r}\r}2z{\r58 = 55.59(\/([5a-5b])\/,5c);\r1m(58==\'3f\' && 50){\r3l +=\"5d:5e(3f=\"+(4x[55]*27)+\");\";\r}2z{\r3l +=58+\":\"+4x[55]+\";\";\r}\r}\r};\r}\r0 5c(5g){\r4 5h=\'\';\r5h = \'-\'+5g.5i();\r1v 5h;\r};\r1v 3l;\r};\r1j.4w();\r}\r})(1g)", "function|fn|kinMaxShow|user_options|var|default_options|height|310|intervalTime|6|switchTime|1000|easing|linear|imageAlign|center|button|switchEvent|click|showIndex|false|normal|width|14px|lineHeight|right|10px|bottom|fontSize|background|cccaca|border|1px|solid|ffffff|color|666666|textAlign|marginRight|8px|fontFamily|Verdana|float|left|focus|CC0000|FF0000|000000|callback|index|action|options|jQuery|extend|true|k|selector|this|if|length|1|error|More|than|one|selected|object|return|self|0|lindex|size|children|div|prename|kinMaxShow_|data|onload|css|100|overflow|hidden|position|relative|addClass|image_item|hide|init|setData|setLayout|setAnimate|title|new|Array|each|push|find|img|attr|alt|wrapAll|class|image_box|a|image|src|remove|else|url|no|repeat|z|eq|display|none|button_list|for|i|li|append|ul|setCSS|gt|opacity|show|visible|visibility|block|cssCode|style|type|text|margin|padding|parseInt|px|absolute|decoration|transparent|indent|outline|expression|hideFocus|objToCss|top|list|2|cursor|pointer|webkit|adjust|default|prepend|call|fadeIn|overDelayTimer|delegate|_this|setChange|setOpacity|mouseover|setTimeout|200|mouseout|clearTimeout|moveTimer|setInterval|fadeOut|clearInterval|removeClass|animated|stop|animate|duration|complete|not|run|obj|excArr|excFlag|isIE|navigator|userAgent|indexOf|MSIE|key|in|inArray|pKey|replace|A|Z|KtoLowerCase|filter|alpha|isArray|word|str|toLowerCase".split("|")));