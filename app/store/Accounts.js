Ext.define("App.store.Accounts", {
    extend: "Ext.data.Store",

    config: {
        model: "App.model.Account",
        sorters: "userName",

        data: [
            { userName: "alanjgorton@googlemail.com", password: "password" },
            { userName: "janedoe@hotmail.com", password: "password" }
        ]
    }
});
