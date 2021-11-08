package com.cybergames.entities

import java.time.LocalDateTime
import javax.persistence.*

@Entity
class Team(
    var name: String,
    @OneToOne var founder: User,
    @OneToOne var captain: User,
    @OneToMany var participants: MutableSet<User>? = null,
    var addedAt: LocalDateTime = LocalDateTime.now(),
    @Id @GeneratedValue var id: Long? = null)

@Entity
class User(
    var login: String,
    var firstname: String,
    var lastname: String,
    var description: String? = null,
    var addedAt: LocalDateTime = LocalDateTime.now(),
    @Id @GeneratedValue var id: Long? = null)

@Entity
class Tournament(
    var name: String,
    var prize: String,
    @OneToOne var genre: Genre,
    @OneToMany var teams: MutableSet<Team>? = null,
    var addedAt: LocalDateTime = LocalDateTime.now(),
    @Id @GeneratedValue var id: Long? = null)

@Entity
class Genre(
    var name: String,
    @Id @GeneratedValue var id: Long? = null)

@Entity
class Game(
    var name: String,
    @OneToOne var tournament: Tournament,
    @OneToMany var teams: MutableSet<Team>? = null,
    @Id @GeneratedValue var id: Long? = null)


