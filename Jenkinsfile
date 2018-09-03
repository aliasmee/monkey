@Library('aistarsea-shared-lib') _
properties([pipelineTriggers([cron('H/15 * * * *')])])
def lib = library('aistarsea-shared-lib').io.aistarsea
import groovy.json.JsonOutput

def mmUtils = lib.MessageLego.new()

def bearyUrl="${env.bearyChatUrl}"
def bearyChan="${env.bearyChatGroup}"

def author = ""
def message = ""
def commitId = ""
def testSummary = ""
def total = 0
def failed = 0
def skipped = 0


log.info 'Starting'
log.warning 'Nothing to do!'
sayHello 'Jenkins'
sayHello ()


node('jenkins-slave-build1') {
    stage ("Test Messages Notify") {
        checkout scm
        chatNotifySend channel: "${bearyChan}", text: "${JOB_NAME} [${BUILD_DISPLAY_NAME}](${BUILD_URL})", endpoint: "${bearyUrl}"

//        println(getCommitAuthor())
//        println(getCommitMsg())
//        println(getCommitHash())
        someMsgTest = mmUtils.commitMsg()
        println(someMsgTest)
        coverage = getTestCoverage('./.last_run.json')
        println("${coverage}")
        testMsg = mmUtils.testMsg("${BRANCH_NAME}", "some test result", "${someMsgTest}",'',mmUtils.colorLegible('good'))
        println(testMsg)
        chatNotifySend attachments: "${testMsg}", channel: "${bearyChan}", text: "${JOB_NAME} [${BUILD_DISPLAY_NAME}](${BUILD_URL})", endpoint: "${bearyUrl}"
        println(currentBuild.currentResult)
    }
}

