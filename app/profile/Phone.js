Ext.define("ZenUsage.profile.Phone", {
    extend: "Ext.app.Profile",

    config: {
        views: [
            "MainView"
        ],

        controllers: [
            "Controller"
        ]
    },

    isActive: function() {
        return Ext.os.is.Phone;
    },

    launch: function() {
        console.log("profile.Phone::launch");
        Ext.create("ZenUsage.view.phone.MainView");
    }
});
