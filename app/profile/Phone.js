Ext.define("App.profile.Phone", {
    extend: "Ext.app.Profile",

    config: {
        views: [
            "App.view.phone.Container"
        ],

        controllers: [
            "Phone",
            "Navigator"
        ]
    },

    isActive: function() {
        return Ext.os.is.Phone;
    },

    launch: function() {
        console.log("profile.Phone::launch");
        Ext.create("App.view.phone.Container");
    }
});
