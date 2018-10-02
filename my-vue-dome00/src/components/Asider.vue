<template>
  <div class="col-2 text-center">
   <nav class="navbar navbar-inverse navbar-fixed-top" id="sidebar-wrapper" role="navigation">
      <ul class="nav sidebar-nav">
        <li class="sidebar-brand"> <a href="#">{{menu_name}}</a> </li>
        <li> <a href="#"> <i class="fa fa-fw fa-home"> </i> Home </a> </li>
        <li> <a href="#"> <i class="fa fa-fw fa-folder"> </i> Page one </a> </li>
        <li> <a href="#"> <i class="fa fa-fw fa-file-o"> </i> Second page </a> </li>
        <li> <a href="#"> <i class="fa fa-fw fa-cog"> </i> Third page </a> </li>
        <li class="dropdown"> <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            <i class="fa fa-fw fa-plus"> </i> Dropdown <span class="caret"> </span> </a>
          <ul class="dropdown-menu" role="menu">
            <li class="dropdown-header"> Dropdown heading </li>
            <li> <a href="#"> Action </a> </li>
            <li> <a href="#"> Another action </a> </li>
            <li> <a href="#"> Something else here </a> </li>
            <li> <a href="#"> Separated link </a> </li>
            <li> <a href="#"> One more separated link </a> </li>
          </ul>
        </li>
        <li> <a href="#"> <i class="fa fa-fw fa-bank"> </i> Page four </a> </li>
        <li> <a href="#"> <i class="fa fa-fw fa-dropbox"> </i> Page 5 </a> </li>
        <li> <a href="#"> <i class="fa fa-fw fa-twitter"> </i> Last page </a> </li>
      </ul>
    </nav>
   <!-- <div class="accordion" id="accordionMenu">
        <div id="headingOne">
            <button id="headingOne" class="btn btn-lg btn-block" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
              MENU Group Item #1
            </button>
        </div>
        <div id="collapseOne" class="collapse show btn-group-vertical" aria-labelledby="headingOne" data-parent="#accordionMenu">
          <button class="btn">
            MENU Item #1-1
          </button>
          <button class="btn btn-outline-primary btn-block">
            MENU Item #1-2
          </button>
          <button class="btn btn-outline-primary btn-block">
            MENU Item #1-3
          </button>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
              MENU Group Item #2
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionMenu">
          <div class="card-body">
            Anim 
          </div>
        </div>
      </div>
      <div class="card">
        <div class="card-header" id="headingThree">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" type="button" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
              MENU Group Item #3
            </button>
          </h5>
        </div>
        <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordionMenu">
          <div class="card-body">
            Anim pariatur
          </div>
        </div>
      </div>
   </div> -->
  </div>
</template>

<script>
export default {
  name: 'Asider',
  data() {
    return {
        menu_name: "MENU",
    }
  },
  props: {
    msg: String,
  },
  mounted() {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*@import "https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css";*/

/*-------------------------------*/
/*           VARIABLES           */
/*-------------------------------*/
.nav .open > a {
  background-color: transparent;
}
.nav .open > a:hover {
  background-color: transparent;
}
.nav .open > a:focus {
  background-color: transparent;
}
/*-------------------------------*/
/*           Wrappers            */
/*-------------------------------*/
#wrapper {
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  -webkit-transition: all 0.5s ease;
  padding-left: 0;
  transition: all 0.5s ease;
}
#wrapper.toggled {
  padding-left: 220px;
}
#wrapper.toggled #sidebar-wrapper {
  width: 220px;
}
#wrapper.toggled #page-content-wrapper {
  margin-right: 0px;
  position: relative;
}
#sidebar-wrapper {
  -moz-transition: all 0.5s ease;
  -o-transition: all 0.5s ease;
  -webkit-transition: all 0.5s ease;
  /*background: #1a1a1a;*/
  height: 100%;
  left: 0px;
  margin-left: 0px;
  overflow-x: hidden;
  overflow-y: auto;
  transition: all 0.5s ease;
  width: 100%;
  /*z-index: 1000;*/
}
#sidebar-wrapper::-webkit-scrollbar {
  display: none;
}
#page-content-wrapper {
  padding-top: 70px;
  width: 100%;
}
/*-------------------------------*/
/*     Sidebar nav styles        */
/*-------------------------------*/
.sidebar-nav {
  list-style: none;
  margin: 0;
  padding: 0;
  position: absolute;
  top: 0;
  width: 100%;
}
.sidebar-nav li {
    color: #CCCCCC;
  display: inline-block;
  line-height: 20px;
  position: relative;
  width: 100%;
}
.sidebar-nav li:before {
  /*background-color: #1c1c1c;*/
  color: #CCCCCC;
  content: '';
  height: 100%;
  left: 0;
  position: absolute;
  top: 0;
  -webkit-transition: width 0.2s ease-in;
  transition: width 0.2s ease-in;
  width: 3px;
  z-index: -1;
}
.sidebar-nav li:first-child a {
  /*background-color: #1a1a1a;*/
  color: #1a1a1a;
}
.sidebar-nav li:nth-child(2):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(3):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(4):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(5):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(6):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(7):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(8):before {
  background-color: #6677cc;
}
.sidebar-nav li:nth-child(9):before {
  background-color: #6677cc;
}
.sidebar-nav li:hover:before {
  -webkit-transition: width 0.2s ease-in;
  transition: width 0.2s ease-in;
  width: 100%;
}
.sidebar-nav li a {
  color: #222222;
  display: block;
  padding: 10px 15px 10px 30px;
  text-decoration: none;
}
.sidebar-nav li.open:hover before {
  -webkit-transition: width 0.2s ease-in;
  transition: width 0.2s ease-in;
  width: 100%;
}
.sidebar-nav .dropdown-menu {
  background-color: #CCCCCC;
  border-radius: 0;
  border: none;
  box-shadow: none;
  margin: 0;
  padding: 0;
  position: relative;
  width: 100%;
}
.sidebar-nav li a:hover,
.sidebar-nav li a:active,
.sidebar-nav li a:focus,
.sidebar-nav li.open a:hover,
.sidebar-nav li.open a:active,
.sidebar-nav li.open a:focus {
  background-color: transparent;
  color: #1a1a1a;
  text-decoration: none;
}
.sidebar-nav > .sidebar-brand {
  font-size: 20px;
  height: 65px;
  line-height: 44px;
}
/*-------------------------------*/
/*       Hamburger-Cross         */
/*-------------------------------*/
.hamburger {
  background: transparent;
  border: none;
  display: block;
  height: 32px;
  margin-left: 15px;
  position: fixed;
  top: 20px;
  width: 32px;
  z-index: 999;
}
.hamburger:hover {
  outline: none;
}
.hamburger:focus {
  outline: none;
}
.hamburger:active {
  outline: none;
}
.hamburger.is-closed:before {
  -webkit-transform: translate3d(0, 0, 0);
  -webkit-transition: all 0.35s ease-in-out;
  color: #222222;
  content: '';
  display: block;
  font-size: 14px;
  line-height: 32px;
  opacity: 0;
  text-align: center;
  width: 100px;
}
.hamburger.is-closed:hover before {
  -webkit-transform: translate3d(-100px, 0, 0);
  -webkit-transition: all 0.35s ease-in-out;
  display: block;
  opacity: 1;
}
.hamburger.is-closed:hover .hamb-top {
  -webkit-transition: all 0.35s ease-in-out;
  top: 0;
}
.hamburger.is-closed:hover .hamb-bottom {
  -webkit-transition: all 0.35s ease-in-out;
  bottom: 0;
}
.hamburger.is-closed .hamb-top {
  -webkit-transition: all 0.35s ease-in-out;
  background-color: rgba(255, 255, 255, 0.7);
  top: 5px;
}
.hamburger.is-closed .hamb-middle {
  background-color: rgba(255, 255, 255, 0.7);
  margin-top: -2px;
  top: 50%;
}
.hamburger.is-closed .hamb-bottom {
  -webkit-transition: all 0.35s ease-in-out;
  background-color: rgba(255, 255, 255, 0.7);
  bottom: 5px;
}
.hamburger.is-closed .hamb-top,
.hamburger.is-closed .hamb-middle,
.hamburger.is-closed .hamb-bottom,
.hamburger.is-open .hamb-top,
.hamburger.is-open .hamb-middle,
.hamburger.is-open .hamb-bottom {
  height: 4px;
  left: 0;
  position: absolute;
  width: 100%;
}
.hamburger.is-open .hamb-top {
  -webkit-transform: rotate(45deg);
  -webkit-transition: -webkit-transform 0.2s cubic-bezier(0.73, 1, 0.28, 0.08);
  /*background-color: #ffffff;*/
  margin-top: -2px;
  top: 50%;
}
.hamburger.is-open .hamb-middle {
  /*background-color: #ffffff;*/
  display: none;
}
.hamburger.is-open .hamb-bottom {
  -webkit-transform: rotate(-45deg);
  -webkit-transition: -webkit-transform 0.2s cubic-bezier(0.73, 1, 0.28, 0.08);
  /*background-color: #ffffff;*/
  margin-top: -2px;
  top: 50%;
}
.hamburger.is-open:before {
  -webkit-transform: translate3d(0, 0, 0);
  -webkit-transition: all 0.35s ease-in-out;
  /*color: #444444;*/
  content: '';
  display: block;
  font-size: 14px;
  line-height: 32px;
  opacity: 0;
  text-align: center;
  width: 100px;
}
.hamburger.is-open:hover before {
  -webkit-transform: translate3d(-100px, 0, 0);
  -webkit-transition: all 0.35s ease-in-out;
  display: block;
  opacity: 1;
}
/*-------------------------------*/
/*          Dark Overlay         */
/*-------------------------------*/
.overlay {
  position: fixed;
  display: none;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.4);
  z-index: 1;
}
/* SOME DEMO STYLES - NOT REQUIRED */
/*body,
html {
  background-color: #583e7e;
}
body h1,
body h2,
body h3,
body h4 {
  color: rgba(255, 255, 255, 0.9);
}
body p,
body blockquote {
  color: rgba(255, 255, 255, 0.7);
}
body a {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: underline;
}
body a:hover {
  color: #ffffff;
}*/

</style>
