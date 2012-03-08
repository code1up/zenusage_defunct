Ext.define("App.store.Services", {
    extend: "Ext.data.Store",

    config: {
        model: "App.model.Service",
        sorters: "alias",

        data: [
            { alias: "Home" },
            { alias: "Office" }
        ]
    }
});
