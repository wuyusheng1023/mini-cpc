(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{120:function(e,t,n){},121:function(e,t,n){},257:function(e,t,n){"use strict";n.r(t);var c=n(0),a=n.n(c),r=n(25),o=n.n(r),s=(n(120),n(121),n(122),n(81)),i=n.n(s),j=n(113),l=n(114),u=n(26),b=n(79),d=n(46),O=n.n(d),h=n(31),f=n.n(h),p=n(112),x=n.n(p),m=n(47),g=n.n(m),w=n(39),S=n.n(w),y=n(260),v=n(261),C=n(110),F=n.n(C),_=n(4);function I(e){var t=e.dataArr,n=t.map((function(e){return e.datetime})),c=t.map((function(e){return e.concentration}));return Object(_.jsx)(F.a,{data:[{x:n,y:c},{type:"scatter"}],layout:{width:520,height:400,yaxis:{title:"Number Concentraion (#/cm3)"}}})}var N="ws://localhost:8765",T=new b.w3cwebsocket(N);function k(){var e=window.location.hostname,t=window.location.port,n="http://".concat(e,":").concat(t,"/api/command"),a=Object(c.useState)(!0),r=Object(u.a)(a,2),o=r[0],s=r[1],i=Object(c.useState)(!1),d=Object(u.a)(i,2),h=d[0],p=(d[1],Object(c.useState)(!1)),m=Object(u.a)(p,2),w=m[0],C=(m[1],Object(c.useState)()),F=Object(u.a)(C,2),k=F[0],D=F[1],P=Object(c.useState)([]),E=Object(u.a)(P,2),A=E[0],z=E[1],J=Object(c.useState)(Date.now()),L=Object(u.a)(J,2),R=L[0],V=L[1];Object(c.useEffect)((function(){var e=o?"on":"off";fetch(n,{method:"POST",headers:{Accept:"application/json, text/plain","Content-Type":"application/json; charset=UTF-8"},body:JSON.stringify(e)}).then((function(e){return e.json()})).then((function(e){return console.log("Post res:",e)})).catch(console.error)}),[o]);var U=function(e){var t=JSON.parse(e.data);console.log(t),D(t),V(Date.now())};T.onmessage=U,function(e,t){var n=Object(c.useRef)();Object(c.useEffect)((function(){n.current=e})),Object(c.useEffect)((function(){if(null!==t){var e=setInterval((function(){n.current()}),t);return function(){return clearInterval(e)}}}),[t])}((function(){if(Date.now()-R>2e3)(T=new b.w3cwebsocket(N)).onmessage=U;else{var e=new Date,t=Object(l.a)({},k);t.datetime=e;var n=Object(j.a)(A);for(n.push(t);Date.parse(e)-Date.parse(n[0].datetime)>=36e5;)n.shift();z(n)}}),2e3);return Object(_.jsxs)(O.a,{children:[Object(_.jsxs)(f.a,{span:8,offset:0,children:[Object(_.jsx)(x.a,{style:{margin:5},defaultChecked:!0,onChange:function(e){s(e)}}),o?w?Object(_.jsx)(g.a,{icon:Object(_.jsx)(y.a,{}),color:"error",children:"ERROR"}):h?Object(_.jsx)(g.a,{icon:Object(_.jsx)(v.a,{}),color:"warning",children:"WARNING"}):null:null,o&&k?Object(_.jsxs)(_.Fragment,{children:[Object(_.jsxs)("h1",{style:{margin:10,padding:10,backgroundColor:"WhiteSmoke"},children:[Object(_.jsx)("p",{style:{fontSize:35,display:"inline"},children:k.concentration.toPrecision(3)}),Object(_.jsx)("span",{children:"\xa0"}),Object(_.jsxs)("p",{style:{fontSize:20,display:"inline"},children:["#/cm",Object(_.jsx)("sup",{children:"3"})]})]}),Object(_.jsxs)(O.a,{children:[Object(_.jsx)(f.a,{span:6,offset:2,children:Object(_.jsx)(S.a,{itemLayout:"horizontal",dataSource:["temp_sat","temp_con","temp_opt","flow"],renderItem:function(e){return Object(_.jsx)(S.a.Item,{children:e})}})}),Object(_.jsx)(f.a,{span:6,offset:2,children:Object(_.jsx)(S.a,{itemLayout:"horizontal",dataSource:[parseFloat(k.saturator_temperature).toFixed(2),parseFloat(k.condensor_temperature).toFixed(2),parseFloat(k.optics_temperature).toFixed(2),parseFloat(k.sample_flow).toFixed(2)],renderItem:function(e){return Object(_.jsx)(S.a.Item,{children:e})}})}),Object(_.jsx)(f.a,{span:6,offset:2,children:Object(_.jsx)(S.a,{itemLayout:"horizontal",dataSource:[Object(_.jsxs)("text",{children:[Object(_.jsx)("sup",{children:"o"}),"C"]}),Object(_.jsxs)("text",{children:[Object(_.jsx)("sup",{children:"o"}),"C"]}),Object(_.jsxs)("text",{children:[Object(_.jsx)("sup",{children:"o"}),"C"]}),Object(_.jsx)("text",{children:"ml/min"})],renderItem:function(e){return Object(_.jsx)(S.a.Item,{children:e})}})})]})]}):null]}),Object(_.jsx)(f.a,{span:11,offset:0,children:o?Object(_.jsx)(I,{dataArr:A}):Object(_.jsx)("h2",{style:{color:"steelblue"},children:"mini_CPC by University of Helsinki"})})]})}var D=n(54),P=n.n(D),E=n(262),A=n(263);function z(e){var t=e.defaultName,n=e.defaultValue,a=e.delta,r=e.onChange,o=void 0===r?function(e){return e}:r,s=Object(c.useState)(t),i=Object(u.a)(s,2),j=i[0],l=(i[1],Object(c.useState)(n)),b=Object(u.a)(l,2),d=b[0],O=b[1];Object(c.useEffect)((function(){O(n)}),[n]),Object(c.useEffect)((function(){o(d)}),[d]);return Object(_.jsxs)("div",{style:{width:75,height:200},children:[Object(_.jsx)(g.a,{style:{width:75,height:40},children:j}),Object(_.jsx)(P.a,{style:{width:75,height:40},icon:Object(_.jsx)(E.a,{}),onClick:function(){if(a>=1){var e=parseInt(d)+parseInt(a);O(e)}else{var t=parseFloat(d)+parseFloat(a);O(parseFloat(t.toFixed(2)))}}}),Object(_.jsx)(g.a,{style:{width:75,height:40},children:d}),Object(_.jsx)(P.a,{style:{width:75,height:40},icon:Object(_.jsx)(A.a,{}),onClick:function(){if(a>=1){var e=parseInt(d)-parseInt(a);O(e)}else{var t=parseFloat(d)-parseFloat(a);O(parseFloat(t.toFixed(2)))}}})]})}function J(){var e=window.location.hostname,t=window.location.port,n="http://".concat(e,":").concat(t,"/api/settings"),a="http://".concat(e,":").concat(t,"/api/set"),r=Object(c.useState)(),o=Object(u.a)(r,2),s=o[0],i=o[1],j=Object(c.useState)(),l=Object(u.a)(j,2),b=l[0],d=l[1],h=Object(c.useState)(),p=Object(u.a)(h,2),x=p[0],m=p[1],g=Object(c.useState)(),w=Object(u.a)(g,2),S=w[0],y=w[1],v=Object(c.useState)(),C=Object(u.a)(v,2),F=C[0],I=C[1],N=Object(c.useState)(),T=Object(u.a)(N,2),k=T[0],D=T[1],E=Object(c.useState)(),A=Object(u.a)(E,2),J=A[0],L=A[1],R=Object(c.useState)(),V=Object(u.a)(R,2),U=V[0],B=V[1],W=function(e){return i(e.saturator_temperature),d(e.condensor_temperature),m(e.optics_temperature),y(e.sample_flow),e};Object(c.useEffect)((function(){fetch(n).then((function(e){return e.json()})).then(W).then(console.log).catch(console.error)}),[]);return Object(_.jsxs)(_.Fragment,{children:[Object(_.jsxs)(O.a,{children:[Object(_.jsx)(f.a,{children:Object(_.jsx)(z,{defaultName:"Sat_T",defaultValue:s||50,delta:1,onChange:function(e){I(e)}})}),Object(_.jsx)(f.a,{children:Object(_.jsx)(z,{defaultName:"Con_T",defaultValue:b||20,delta:1,onChange:function(e){D(e)}})}),Object(_.jsx)(f.a,{children:Object(_.jsx)(z,{defaultName:"Opt_T",defaultValue:x||50,delta:1,onChange:function(e){L(e)}})}),Object(_.jsx)(f.a,{children:Object(_.jsx)(z,{defaultName:"flow",defaultValue:S||.1,delta:.01,onChange:function(e){B(e)}})})]}),Object(_.jsx)(O.a,{children:Object(_.jsx)(P.a,{onClick:function(){var e={saturator_temperature:F,condensor_temperature:k,optics_temperature:J,sample_flow:U};fetch(a,{method:"POST",headers:{Accept:"application/json, text/plain","Content-Type":"application/json; charset=UTF-8"},body:JSON.stringify(e)}).then((function(e){return e.json()})).then((function(e){return console.log("Post res:",e)})).catch(console.error)},children:"Confirm"})})]})}var L=i.a.TabPane;function R(){return Object(_.jsxs)(i.a,{type:"card",defaultActiveKey:"1",children:[Object(_.jsx)(L,{tab:"Dashboard",children:Object(_.jsx)(k,{})},"1"),Object(_.jsx)(L,{tab:"Setting",children:Object(_.jsx)(J,{})},"2"),Object(_.jsx)(L,{tab:"Data",children:"3"},"3")]})}var V=function(){return Object(_.jsx)("div",{className:"App",children:Object(_.jsx)(R,{})})},U=function(e){e&&e instanceof Function&&n.e(3).then(n.bind(null,264)).then((function(t){var n=t.getCLS,c=t.getFID,a=t.getFCP,r=t.getLCP,o=t.getTTFB;n(e),c(e),a(e),r(e),o(e)}))};o.a.render(Object(_.jsx)(a.a.StrictMode,{children:Object(_.jsx)(V,{})}),document.getElementById("root")),U()}},[[257,1,2]]]);
//# sourceMappingURL=main.ec03720f.chunk.js.map