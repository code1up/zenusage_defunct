Ext.define("App.controller.tablet.Navigator", {
    extend: "App.controller.NavigatorBase",

    config: {
        refs: {
            // Container
            navigator: "navigator",

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

                    this.getEditButton().hide();
                    this.getDoneButton().show();
                    this.getAddButton().show();
                }
            },

            doneButton: {
                tap: function() {
                    console.log("App::controller::Navigator::editButton::tap");

                    this.getEditButton().show();
                    this.getDoneButton().hide();
                    this.getAddButton().hide();
                }
            },

            backButton: {
                tap: function() {
                    this.getNavigator().setActiveItem(0);
                }
            },

            accountList: {
                itemtap: function(list, index, target, record, event) {
                    console.log("Navigator::accountList::itemtap");

                    this.getBackButton().show();
                    this.getEditButton().hide();
                    this.getDoneButton().hide();
                    this.getAddButton().hide();

                    this.getNavigator().setActiveItem(1);
                }
            }
        }
    },

    launch: function() {
        this.callParent(arguments);
    }
});
