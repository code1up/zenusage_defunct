Ext.define("App.controller.phone.Phone", {
    extend: "App.controller.Base",

    config: {
        refs: {
            phoneContainer: "phonecontainer",
            serviceList: "navigator #serviceList"
      },

        control: {
            serviceList: {
                itemtap: function(list, index, target, record, event) {
                    console.log("Phone::serviceList::itemtap");

                    /*
                     cardLayout.setActiveItem(1, {type: 'slide', direction: 'left', complete: test});
function test() {
alert('ok !');
}
                    */

                    this.getPhoneContainer().setActiveItem(1);
                }
            }
        }
    },

    launch: function() {
        this.callParent(arguments);
    }
});
