@Library('aistarsea-shared-lib') _

def bearyUrl="${env.bearyChatUrl}"
def bearyChan="${env.bearyChatGroup}"


log.info 'Starting'
log.warning 'Nothing to do!'
sayHello 'Jenkins'
sayHello ()
node('jenkins-slave-build1') {
  chatNotifySend channel: "@${bearyChan}", text: "this messages from jenkins", endpoint: "${bearyUrl}"
}
