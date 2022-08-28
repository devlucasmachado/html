class mobilebar {
    constructor(mobilemenu, navlist, navlinks) {
        this.mobilemenu = document.querySelector(mobilemenu)
        this.navlist = document.querySelector(navlist)
        this.navlinks = document.querySelectorAll(navlinks)
        this.activeClass = "active"
        this.handleclick = this.handleclick.bind(this)
    }
    
    handleclick(){
        console.log(this);
        this.navlist.classList.toggle(this.activeClass)
        this.mobilemenu.classList.toggle(this.activeClass)
    }

    addclickevent() {
        this.mobilemenu.addEventListener("click", this.handleclick)
    }
    
    init(){
        if(this.mobilemenu){
            this.addclickevent()
        }
        return this
    }
}
const mobile = new mobilebar(".menu", 
"#nav-list", 
"#nav-list li")

mobile.init()