const qrcode = require('qrcode-terminal');
const { Client, LocalAuth } = require('whatsapp-web.js');
const client = new Client({
    authStrategy: new LocalAuth()
});

client.once('qr', qr => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});

let awaitingUserResponse = false; // Track if bot is waiting for a user response

client.on('message', async message => {
    const userInput = message.body.toLowerCase();

    if (awaitingUserResponse) {
        // Handle user response based on the last query
        if (userInput === "1" || userInput === "job search") {
            await message.reply("Here are companies that are most suited for your inclusivity needs within the tech industry:\n- Unilever\n- Box Fusion\n- Chenosis\n- Nestlé \n-Vumatel\n- Mint\n\nFind out more about their policies here: [hyperlink to web app]\n\nClick this link to be directed to our website to get assistance for job searches: [officeally.com/Job+Search](https://officeally.com/Job+Search)");
        } else if (userInput === "2" || userInput === "know your rights as an employee") {
            await message.reply("Here are a few that rights you are entitled to within the workplace:\n1. Equal Pay: Women have the right to receive equal pay for equal work. This means that employers cannot pay female employees less than their male counterparts for performing the same job with the same qualifications and experience.\n2. Protection Against Discrimination: Women are protected against discrimination based on their gender. This includes hiring, firing, promotions, assignments, and all other aspects of employment.\n3. Freedom from Harassment: Women have the right to work in an environment free from sexual harassment, including unwelcome advances, comments, or actions that create a hostile or uncomfortable workplace.\n4. Pregnancy and Maternity Rights: Women are entitled to protections during pregnancy and maternity leave. This includes the right to reasonable accommodations, job protection during maternity leave, and the ability to return to the same or equivalent position after leave.\n5. Flexible Work Arrangements: Many workplaces offer flexible work arrangements, such as telecommuting or flexible hours, to accommodate family responsibilities and work-life balance needs.\n\nIf you would like to view more rights related to women in the workplace, click on this link: [enters link]");
        } else if (userInput === "3" || userInput === "tips for recruiters") {
            await message.reply("Looking for recruitment?");
        } else if (userInput === "4" || userInput === "faqs") {
            await message.reply("FAQs\nQ1. How can I address gender pay disparities or unequal treatment?\nAnswer: Discuss pay disparities or unequal treatment with your HR department. Many jurisdictions have laws against pay discrimination. Gather evidence and initiate a conversation about rectifying the situation.\n\nQ2. What resources are available to help me understand my rights related to gender equality in the workplace?\nAnswer: Consult your company's policies and handbooks for information on gender equality. Research your local labor laws and regulations that address workplace discrimination and gender-based issues.\n\nQ3. How can I address comments or behaviors that contribute to a sexist work environment?\nAnswer: If you encounter sexist comments or behaviors, address them professionally but firmly. Educate colleagues about the impact of their words and actions. If the behavior persists, report it to your supervisor or HR.\n\nQ4. Can I seek mentorship or guidance to navigate gender-related challenges at work?\nAnswer: Absolutely. Seek out mentors, both within and outside your organization, who can provide guidance and support as you navigate gender-related challenges. Networking and mentorship can offer valuable insights and advice.\n\nQ5.  What can I do if my work-life balance is affected by gender-related challenges, such as family expectations or caregiving responsibilities?\nAnswer: Communicate your work-life balance needs with your supervisor. Many workplaces offer flexible arrangements to accommodate family and caregiving responsibilities. Seek assistance from Employee Assistance Programs (EAPs) if available.");
        } else {
            await message.reply("I'm sorry, you made an invalid selection. Please make choose a valid option number or keyword.");
        }
        
        awaitingUserResponse = false; // Reset the flag
    } else {
        if (userInput === "hey there allybot") {
            await message.reply("Hi there! I am AllyBot and I am here to assist:).\nSelect an option using the option number or keyword.\n1. Menu\n2. About");
        } else if (userInput === "2" || userInput === "about") {
            await message.reply("AllyBot was created by a team of tech enthusiasts who believe in the importance of inclusivity and accessibility...");
        } else if (userInput === "1" || userInput === "menu") {
            await message.reply("Menu\n1. Job search\n2. Know your rights as an employee\n3. Tips for recruiters\n4. FAQs");
            awaitingUserResponse = true; // Set the flag to true to await user response
        }
    }
});
client.initialize();
