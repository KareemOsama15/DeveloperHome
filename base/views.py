from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article, Resource, Question, Comment
from .forms import ArticleForm, ResourceForm, QuestionForm, CommentForm

def home(request):
    articles = Article.objects.all()
    resources = Resource.objects.all()
    questions = Question.objects.all()

    for article in articles:
        article.content = article.content[:70]

    for question in questions:
        question.content = question.content[:70]

    

    if request.method == 'POST':
        deleteArticle_id = request.POST.get('deleteArticle-id')
        deleteResource_id = request.POST.get('deleteResource-id')
        deleteQuestion_id = request.POST.get('deleteQuestion-id')


        if deleteArticle_id:
            article_post = Article.objects.filter(id=deleteArticle_id).first()
            if article_post and request.user == article_post.author:
                article_post.delete()
                return redirect('home')

        if deleteResource_id:
            resource_post = Resource.objects.filter(id=deleteResource_id).first()
            if resource_post and request.user == resource_post.author:
                resource_post.delete()
                return redirect('home')

        if deleteQuestion_id:
            question_post = Question.objects.filter(id=deleteQuestion_id).first()
            if question_post and request.user == question_post.author:
                question_post.delete()
                return redirect('home')

    context = {
        'articles': articles,
        'resources': resources,
        'questions': questions,
        'article_type': 'Article',
        'resource_type': 'Resource',
        'question_type': 'Question',
    }
    return render(request, 'base/home.html', context=context)

def about(request):
    return render(request, 'base/about.html')

def landingPage(request):
    return render(request, 'base/landingPage.html')

@login_required(login_url="/login")
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('articles')
    else:
        form = ArticleForm()
    context = {
        'title': 'Article',
        'form': form
    }
    return render(request, 'base/create_post.html', context=context)

@login_required(login_url="/login")
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.save()
            return redirect('questions')
    else:
        form = QuestionForm()
    context = {
        'title': 'Question',
        'form': form,
    }
    return render(request, 'base/create_post.html', context=context)

@login_required(login_url="/login")
def create_resource(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.author = request.user
            resource.save()
            return redirect('resources')
    else:
        form = ResourceForm()
    context = {
        'title': 'Resource',
        'form': form,
    }
    return render(request, 'base/create_post.html', context=context)

def display_articles(request):
    articles = Article.objects.all()
    for article in articles:
        article.content = article.content[:70]

    if request.method == 'POST':
        # likeArticle_id = request.POST.get('likeArticle-id')
        deleteArticle_id = request.POST.get('deleteArticle-id')

        if deleteArticle_id:
            article_post = Article.objects.filter(id=deleteArticle_id).first()
            if article_post and request.user == article_post.author:
                article_post.delete()
                return redirect('articles')

        # if likeArticle_id:
        #     article_post = Article.objects.filter(id=likeArticle_id).first()
        #     if article_post:
        #         article_post.likes += 1
        #         article_post.save()

    context = {
        'title': 'Article',
        'articles': articles
    }
    return render(request, 'base/articles.html', context=context)
    

def display_resources(request):
    resources = Resource.objects.all()
    
    if request.method == 'POST':
        deleteResource_id = request.POST.get('deleteResource-id')

        if deleteResource_id:
            resource_post = Resource.objects.filter(id=deleteResource_id).first()
            if resource_post and request.user == resource_post.author:
                resource_post.delete()
                return redirect('resources')

    context = {
        'title': 'Resource',
        'resources': resources
    }
    return render(request, 'base/resources.html', context=context)

def display_questions(request):
    questions = Question.objects.all()
    for question in questions:
        question.content = question.content[:70]

    # Delete operation
    if request.method == 'POST':
        deleteQuestion_id = request.POST.get('deleteQuestion-id')

        if deleteQuestion_id:
            question_post = Question.objects.filter(id=deleteQuestion_id).first()
            if question_post and request.user == question_post.author:
                question_post.delete()
                return redirect('questions')
    context = {
        'title': 'Question',
        'questions': questions
    }
    return render(request, 'base/questions.html', context=context)

def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = Comment.objects.filter(post=article)

    print('check if there is a post method')
    if request.method == 'POST' and article:
        print('Article exist and post method')
        form = CommentForm(request.POST)
        print()
        print(form)
        if form.is_valid():
            print('form is valid')
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = article
            comment.save()
            print('comment saved')
            return redirect('view-article', article_id)
        else:
            print(form.errors)
    else:
        form = CommentForm()
    context = {
        'article': article,
        'form': form,
        'comments': comments,
    }
    return render(request, 'base/view_article.html', context=context)


def view_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    context = {
        'resource': resource
    }
    return render(request, 'base/view_resource.html', context=context)

def view_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'base/view_question.html', context=context)
