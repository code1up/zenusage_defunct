(function() {
    var backButton = Ext.create("Ext.Button", {
        id: "backButton",
        ui: "back",
        text: "Back",
        align: "left",
        hidden: true
    });

    var addButton = Ext.create("Ext.Button", {
        id: "addButton",
        ui: "confirm",
        text: "Add",
        align: "left",
        hidden: true
    });

    var editButton = Ext.create("Ext.Button", {
        id: "editButton",
        text: "Edit",
        align: "right"
    });

    var doneButton = Ext.create("Ext.Button", {
        id: "doneButton",
        ui: "action",
        text: "Done",
        align: "right",
        hidden: true
    });

    var titleBar = Ext.create("Ext.TitleBar", {
        xtype: "titlebar",
        id: "titlebar",
        docked: "top",
        title: "Accounts",

        items: [
            backButton,
            addButton,
            editButton,
            doneButton
        ]
    });

    Ext.define("App.view.Navigator", {
        extend: "Ext.Panel",
        xtype: "navigator",

        config: {
            layout: {
                type: "card",
                animation: "slide" // TODO
            },

            autoDestroy: false, // TODO: why?

            items: [
                titleBar,
                {
                    xtype: "accountlist",
                    id: "accountList"
                },
                {
                    xtype: "servicelist",
                    id: "serviceList"
                }
            ]
        }
    });
})();
