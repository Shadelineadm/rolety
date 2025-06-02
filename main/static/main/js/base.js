$(function(){
    $('.menu_open').click(function(){
        $('.nav').toggleClass('show_nav');
        $('.nav_el').toggleClass('nav_el2');
        $('.current_page').toggleClass('current_page2');
    })
});