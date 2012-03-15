Ext.define("App.controller.NavigatorBase", {
    extend: "Ext.app.Controller",

    config: {
        mode: null,

        refs: {
            // Container
            navigator: "navigator",

            // Toolbar
            titlebar: "navigator #titlebar",

            // Buttons
            backButton: "navigator #backButton",
            addButton: "navigator #addButton",
            doneButton: "navigator #doneButton",
            editButton: "navigator #editButton",

            // Lists
            accountList: "navigator #accountList",
            serviceList: "navigator #serviceList"
        },

        control: {
            editButton: {
                tap: function() {
                    console.log("App::controller::Navigator::editButton::tap");

                    this.setMode("editaccounts");
                }
            },

            doneButton: {
                tap: function() {
                    console.log("App::controller::Navigator::editButton::tap");

                    this.setMode("viewaccounts");
                }
            },

            backButton: {
                tap: function() {
                    this.getNavigator().setActiveItem(0);

                    this.setMode("viewaccounts");
                }
            },

            accountList: {
                itemtap: function(list, index, target, record, event) {
                    console.log("Navigator::accountList::itemtap");

                    switch (this.getMode()) {
                        case "viewaccounts":
                            this.setMode("viewservices");
                            break;

                        case "editaccounts":
                            this.showAccountMenu(target);
                            break;
                    }
                }
            }
        }
    },

    updateMode: function(mode) {
        var title = "Accounts";
        var activeItem = 0;

        var back = false;
        var edit = false;
        var done = false;
        var add = false;

        switch (mode) {
            case "viewaccounts":
                edit = true;
                break;

            case "editaccounts":
                done = add = true;
                break;

            case "viewservices":
                back = true;

                title = "Services";
                activeItem = 1;
                break;
        }

        this.getTitlebar().setTitle(title);
        this.setActiveItem(activeItem);

        this.getBackButton().setHidden(!back);
        this.getEditButton().setHidden(!edit);
        this.getDoneButton().setHidden(!done);
        this.getAddButton().setHidden(!add);
    },

    // TODO: utility
    setActiveItem: function(index) {
        var navigator = this.getNavigator();

        if (navigator.getActiveItem() !== index) {
            navigator.setActiveItem(index);
        }
    },

    showAccountMenu: function(target) {
        var menu = Ext.create("Ext.Panel", {
            layout: {
                type: "vbox"
            },
            floating: true,
            modal: true,
            width: 256,
            scroll: false,

            items: [
                {
                    xtype: "button",
                    ui: "decline",
                    text: "Delete",
                    style: "margin: 2px;"
                },
                {
                    xtype: "button",
                    // ui: "action",
                    text: "Set Credentials",
                    style: "margin: 2px;"
                }
            ]
        });

        menu.showBy(target);
    },

    launch: function() {
        console.log("App::controller::NavigatorBase::launch");

        this.setMode("viewaccounts");
    }
});
