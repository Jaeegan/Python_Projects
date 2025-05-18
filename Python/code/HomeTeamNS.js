javascript:{
    try {
        var IU = document.getElementById('input-15');
        IU.value = 715903797; 
        IU.dispatchEvent(new Event('input', {bubbles: true}));

        const CC = document.getElementById('input-19');
        CC.value = 71111740147381006;
        CC.dispatchEvent(new Event('input', {bubbles: true}));

        // Check Status Button
        document.querySelector('.v-btn__content').click();
    }
    catch {
        throw "Please refresh page and run shortcut again."
    }

    try {
        const ExistsRegistration = document.querySelector('.v-alert__content');
        var Message = ExistsRegistration.textContent;
    }
    catch {} // Ignore exception

    if (Message = "The IU No. or Cash Card Number has been registered, you don't have to register again.") {}
    else {
        const NAME = document.getElementById('input-33');
        NAME.value = 'Joseph Gan';
        NAME.dispatchEvent(new Event('input', {bubbles: true}));

        const MOBILE = document.getElementById('input-37');
        MOBILE.value = 97107958;
        MOBILE.dispatchEvent(new Event('input', {bubbles: true}));

        const SAFRA_ID = document.getElementById('input-41');
        SAFRA_ID.value = 'A200287379';
        SAFRA_ID.dispatchEvent(new Event('input', {bubbles: true}));

        const VEHICLE = document.getElementById('input-45');
        VEHICLE.value = 'FBQ5939X';
        VEHICLE.dispatchEvent(new Event('input', {bubbles: true}));

        // Check Terms&Conditions Button
        document.evaluate(
            '//*[@id="app"]/div[1]/div[1]/div[2]/form/div[9]/div/div/div/div[1]/div/div',
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null,
        ).singleNodeValue.click();

        // Continue Button
        document.evaluate(
            '//*[@id="app"]/div[1]/div[1]/div[2]/form/div[10]/div/button/span',
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null,
        ).singleNodeValue.click();

        const SuccessRegistration = document.querySelector('.v-alert_content)');
        var Message = SuccessRegistration.textContent;
    }
}

completion(Message);
