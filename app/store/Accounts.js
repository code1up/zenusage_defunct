Ext.define("ZenUsage.store.Accounts", {
    extend: "Ext.data.Store",

    config: {
        model: "ZenUsage.model.Account",
        sorters: "userName",

        data: [
            { userName: "alanjgorton@googlemail.com", password: "password" },
            { userName: "janedoe@hotmail.com", password: "password" }
        ]
    }
});
