"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[500],{24568:function(X,x,a){a.r(x),a.d(x,{default:function(){return Q}});var z=a(90228),l=a.n(z),I=a(87999),S=a.n(I),L=a(48305),Z=a.n(L),d=a(75271),p=a(97529),T=a(31102),R=a(32768),$=a(19986),G=a(26068),A=a.n(G),M=a(11784),N=a(9224),C=a(25403),t=a(52676),D={api:""},O=function(v){var r=(0,p.useLocation)(),s=C.Z.parse(r.search),f=A()(A()({},D),v),e=f.api,g=(0,d.useState)(""),c=Z()(g,2),m=c[0],o=c[1],i=(0,p.useModel)("pageLoading"),h=i.setPageLoading,u=function(){var W=S()(l()().mark(function E(){var j,P;return l()().wrap(function(n){for(;;)switch(n.prev=n.next){case 0:if(e){n.next=3;break}return o("The initialization API cannot be null!"),n.abrupt("return");case 3:return j={},Object.keys(s).forEach(function(y){y!=="api"&&(j[y]=s[y])}),h(!0),n.next=8,(0,M.U)({url:e,data:j});case 8:P=n.sent,o(P),h(!1);case 11:case"end":return n.stop()}},E)}));return function(){return W.apply(this,arguments)}}();return(0,d.useEffect)(function(){u()},[e,s.timestamp]),(0,t.jsx)(N.Z,{body:m})},U=O,B=a(92804),F=a(16483),H=a.n(F),Y=a(81414),J={loading:"loading___z87bD"},K=function(){var v=(0,p.useLocation)(),r=C.Z.parse(v.search),s=(0,d.useState)(String),f=Z()(s,2),e=f[0],g=f[1];H().locale("zh-cn");var c=function(){var m=S()(l()().mark(function o(){var i;return l()().wrap(function(u){for(;;)switch(u.prev=u.next){case 0:i="/api/admin/login/index/index",r!=null&&r.api&&(i=r.api),g(i);case 3:case"end":return u.stop()}},o)}));return function(){return m.apply(this,arguments)}}();return(0,d.useEffect)(function(){c()},[v.search]),(0,t.jsx)(T.ZP,{locale:B.Z,children:(0,t.jsx)(R.Z,{children:e?(0,t.jsx)(U,{api:e}):(0,t.jsx)("div",{className:J.loading,children:(0,t.jsx)($.Z,{})})})})},Q=K}}]);
