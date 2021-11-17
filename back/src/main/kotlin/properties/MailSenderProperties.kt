package com.cybergames.properties

import org.springframework.boot.context.properties.ConfigurationProperties
import org.springframework.context.annotation.Configuration

@Configuration
@ConfigurationProperties(prefix = "mail-sender")
class MailSenderProperties {
    lateinit var host: String
    var port: Int = 0
    lateinit var username: String
    lateinit var password: String
    lateinit var protocol: String
    var auth: Boolean = false
    var starttlsEnable: Boolean = false
    var debug: Boolean = false
}