@Library('aistarsea-shared-lib') _
// triggers pipeline worked at every 3rd minute
// properties([pipelineTriggers([cron('H/3 * * * *')])])
// at every 3rd minute only change
//properties([pipelineTriggers([pollSCM('H/3 * * * *')])])

properties(
    [
        [
            $class: 'BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '20']
        ],
        pipelineTriggers([pollSCM('H/3 * * * *')])
    
    ]
)

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

