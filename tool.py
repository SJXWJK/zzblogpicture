#post-instagram{
    padding: 30px;
}
#post-instagram .article-entry{
    padding-right: 0;
}
.instagram{
    position: relative;
    min-height: 500px;
}
.instagram img {
    width: 100%;
}
.instagram .year {
    font-size: 16px;
}
.instagram .open-ins{
    padding: 10px 0;
    color: #cdcdcd;
}
.instagram .open-ins:hover{
    color: #657b83;
}
.instagram .year{
    display: inline;
}
.instagram .thumb {
    width: 25%;
    height: 0; 
    padding-bottom: 25%;
    position: relative;
    display: inline-block;
    text-align: center;
    background: #ededed;
    outline: 1px solid #ddd;
}
.instagram .thumb a {
    position: relative;
}
.instagram .album h1 em{
    font-style: normal;
    font-size: 14px;
    margin-left: 10px;
}
.instagram .album ul{
    display: flex;
    flex-wrap: wrap;
    clear: both;
    width: 100%;
    text-align: left;
}
.instagram .album li{
    list-style: none;
    display: inline-block;
    box-sizing: border-box;
    padding: 0 5px;
    margin-bottom: -10px;
    height: 0;
    width: 25%;
    position: relative;
    padding-bottom: 25%;
}
.instagram .album li:before{
    display: none;
}
.instagram .album div.img-box{
    position: absolute;
    width: 90%;
    height: 90%;
    -webkit-box-shadow: 0 1px 0 rgba(255,255,255,0.4), 0 1px 0 1px rgba(255,255,255,0.1);
    -moz-box-shadow: 0 1px 0 rgba(255,255,255,0.4), 0 1px 0 1px rgba(255,255,255,0.1);
    box-shadow: 0 1px 0 rgba(255,255,255,0.4), 0 1px 0 1px rgba(255,255,255,0.1);
}
.instagram .album div.img-box img{
    width: 100%;
    height: 100%;
    position: absolute;
    z-index: 2;
}
.instagram .album div.img-box .img-bg{
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0px;
    width: 100%;
    margin: -5px;
    padding: 5px;
    -webkit-box-shadow: 0 0 0 1px rgba(0,0,0,.04), 0 1px 5px rgba(0,0,0,0.1);
    -moz-box-shadow: 0 0 0 1px rgba(0,0,0,.04), 0 1px 5px rgba(0,0,0,0.1);
    box-shadow: 0 0 0 1px rgba(0,0,0,.04), 0 1px 5px rgba(0,0,0,0.1);
    -webkit-transition: all 0.15s ease-out 0.1s;
    -moz-transition: all 0.15s ease-out 0.1s;
    -o-transition: all 0.15s ease-out 0.1s;
    transition: all 0.15s ease-out 0.1s;
    opacity: 0.2;
    cursor: pointer;
    display: block;
    z-index: 3;
}
.instagram .album div.img-box .icon {
    font-size: 14px;
    position: absolute;
    left: 50%;
    top: 50%;
    margin-left: -7px;
    margin-top: -7px;
    color: #999;
    z-index: 1;
}
.instagram .album div.img-box .img-bg:hover{
    opacity: 0;
}
.photos-btn-wrap {
    border-bottom: 1px solid #e5e5e5;
    margin-bottom: 20px;
}
.photos-btn {
    font-size: 16px;
    color: #333;
    margin-bottom: -4px;
    padding: 5px 8px 3px;
}
.photos-btn.active {
    color: #08c;
    border: 1px solid #e5e5e5;
    border-bottom: 5px solid #fff;
}

@media screen and (max-width:600px) {
    .instagram .thumb {
        width: 50%;
        padding-bottom: 50%;
    }
    .instagram .album li {
        width: 100%;
        position: relative;
        padding-bottom: 100%;
        text-align: center;
    }
    .instagram .album div.img-box{
        margin: 0;
        width: 90%;
        height: 90%;
    }
}