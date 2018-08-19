@Library('aistarsea-shared-lib') _
import groovy.json.JsonOutput

def bearyUrl="${env.bearyChatUrl}"
def bearyChan="${env.bearyChatGroup}"


log.info 'Starting'
log.warning 'Nothing to do!'
sayHello 'Jenkins'
sayHello ()

node('jenkins-slave-build1') {

  chatNotifySend channel: "${bearyChan}", text: "**this messages from jenkins", endpoint: "${bearyUrl}"
}



def notifyBearychat(text, channel, attachments) {

    def payload = JsonOutput.toJson([text: text,
        channel: channel,
        username: "Jenkins",
        attachments: attachments
    ])

    sh "curl -X POST --data-urlencode \'payload=${payload}\' ${env.bearyChatUrl}"
}

node ('jenkins-slave-build1') {
    stage("Post to beary") {
       notifyBearychat("Success!", "${bearyChan}" , [])
    }
}
