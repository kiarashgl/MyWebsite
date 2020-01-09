function hello() {
    var name=window.prompt("با سلام!\n لطفا نام خود را وارد کنید.");
    if(name==null || name=="") name="بی نام و نشان"
    window.alert( "سلام "+name+ " عزیز!!!")
}