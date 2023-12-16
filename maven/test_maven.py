from maven import parse_output

failure = """  .   ____          _            __ _ _
	name: default
	...]
Starting ChromeDriver 120.0.6099.71 (9729082fe6174c0a371fc66501f5efc5d69d3d2b-refs/branch-heads/6099_56@{#13}) on port 32378
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
[ERROR] Tests run: 1, Failures: 1, Errors: 0, Skipped: 0, Time elapsed: 0 s <<< FAILURE! - in com.example.app.model.PostTest
[ERROR] postHasContent(com.example.app.model.PostTest)  Time elapsed: 0 s  <<< FAILURE!
java.lang.AssertionError:

Expected: a string containing "booo"
but: was "hello"
	at com.example.app.model.PostTest.postHasContent(PostTest.java:14)

[ERROR] Failures:
[ERROR]   PostTest.postHasContent:14
Expected: a string containing "booo"
but: was "hello"
[ERROR] Tests run: 2, Failures: 1, Errors: 0, Skipped: 0
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.1:test (default-test) on project app-template: There are test failures.
[ERROR]
[ERROR] Please refer to /Users/me/code/app-java-template/target/surefire-reports for the individual test results.
[ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException"""


def test_parse_failures():
    expected = ["1 passed 1 failed", "Got \"hello\"", "Expected a string containing \"booo\"",
                "Test is   PostTest.postHasContent line 14"]
    lines = failure.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


success = """2023-12-11 16:56:10.949  INFO 44672 --- [           main] SignUpTest                               : Started SignUpTest in 6.958 seconds (JVM running for 7.268)
Starting ChromeDriver 120.0.6099.71 (9729082fe6174c0a371fc66501f5efc5d69d3d2b-refs/branch-heads/6099_56@{#13}) on port 6725
Only local connections are allowed.
Please see https://chromedriver.chromium.org/security-considerations for suggestions on keeping ChromeDriver safe.
ChromeDriver was started successfully.
2023-12-11 16:56:24.114  INFO 44672 --- [ null to remote] o.o.selenium.remote.ProtocolHandshake    : Detected dialect: W3C
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 21.44 s - in SignUpTest
[INFO] Running com.example.app.model.PostTest
[INFO] Tests run: 1, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0 s - in com.example.app.model.PostTest
2023-12-11 16:56:25.300 DEBUG 44672 --- [       Thread-3] o.s.w.c.s.GenericWebApplicationContext   : Closing org.springframework.web.context.support.GenericWebApplicationContext@492691d7, started on Mon Dec 11 16:56:09 GMT 2023
2023-12-11 16:56:25.302  INFO 44672 --- [       Thread-3] o.s.s.concurrent.ThreadPoolTaskExecutor  : Shutting down ExecutorService 'applicationTaskExecutor'
2023-12-11 16:56:25.304  INFO 44672 --- [       Thread-3] j.LocalContainerEntityManagerFactoryBean : Closing JPA EntityManagerFactory for persistence unit 'default'
2023-12-11 16:56:25.306  INFO 44672 --- [       Thread-3] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown initiated...
2023-12-11 16:56:25.307  INFO 44672 --- [       Thread-3] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Shutdown completed.
[INFO]
[INFO] Results:
[INFO]
[INFO] Tests run: 2, Failures: 0, Errors: 0, Skipped: 0
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  22.724 s
[INFO] Finished at: 2023-12-11T16:56:25Z
[INFO] ------------------------------------------------------------------------"""


def test_parse_success():
    expected = ["2 passed 0 failed"]
    lines = success.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected


multi_failures = """[INFO]
[INFO] -------------------------------------------------------
[INFO]  T E S T S
[INFO] -------------------------------------------------------
[INFO] Running com.example.app.model.PostTest
[ERROR] Tests run: 3, Failures: 2, Errors: 0, Skipped: 0, Time elapsed: 0.024 s <<< FAILURE! - in com.example.app.model.PostTest
[ERROR] postHasContentMore(com.example.app.model.PostTest)  Time elapsed: 0.005 s  <<< FAILURE!
java.lang.AssertionError:

Expected: a string containing "b"
but: was "hello"
	at com.example.app.model.PostTest.postHasContentMore(PostTest.java:24)

[ERROR] postHasContentNo(com.example.app.model.PostTest)  Time elapsed: 0 s  <<< FAILURE!
java.lang.AssertionError:

Expected: a collection containing <Post(id=null, content=d)>
but: was <Post(id=null, content=hello)>, was <Post(id=null, content=hello)>, was <Post(id=null, content=hello)>
	at com.example.app.model.PostTest.postHasContentNo(PostTest.java:35)

[INFO]
[INFO] Results:
[INFO]
[ERROR] Failures:
[ERROR]   PostTest.postHasContentMore:24
Expected: a string containing "b"
but: was "hello"
[ERROR]   PostTest.postHasContentNo:35
Expected: a collection containing <Post(id=null, content=d)>
but: was <Post(id=null, content=hello)>, was <Post(id=null, content=hello)>, was <Post(id=null, content=hello)>
[INFO]
[ERROR] Tests run: 3, Failures: 2, Errors: 0, Skipped: 0
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  1.123 s
[INFO] Finished at: 2023-12-12T15:55:46Z
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.22.1:test (default-test) on project test-project: There are test failures.
[ERROR]
[ERROR] Please refer to /Users/me/code/project/target/surefire-reports for the individual test results.
[ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException"""


def test_multi_failures():
    expected = ["1 passed 2 failed",
                "Got <Post(id=null, content=hello)>, was <Post(id=null, content=hello)>, was <Post(id=null, content=hello)>",
                "Expected a collection containing <Post(id=null, content=d)>",
                "Test is   PostTest.postHasContentNo line 35",
                "Got \"hello\"",
                "Expected a string containing \"b\"",
                "Test is   PostTest.postHasContentMore line 24"]
    lines = multi_failures.split('\n')
    lines.reverse()
    results = parse_output(lines)
    assert results == expected